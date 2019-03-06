""""
Nicholas Lutsko -- EAPS Department, MIT

Parallelized code for 2-layer QG model, 
with non-linear terms calculated using the
Orszag (1971) alias-free transform method. 
Leapfrog time-stepping is used and all terms 
are treated explicitly except for the hyperdiffusion.

Here the model is forced by interacting with a
zonally-uniform mean-flow, as well as by surface 
friction and radiative damping, following Panetta
& Held (1988), but this can be easily changed 
by modifying the "lterm" function. 

To run do, e.g.:
mpiexec -n 4 python parallel_full_NL_QG_model.py

Last updated -- March 6th 2019
"""

from mpi4py import MPI
import numpy as np
import matplotlib.pylab as plt
import math 
from random import random


#######################################################
#  Declare some parameters, arrays, etc.

opt = 3 # 1 = just the linear parts, 2 = just the nonlinear parts, 3 = full model

dt = 0.025 #Timestep
ts = int( 500 / dt ) #Total timesteps
lim = int( 400 / dt) #Start taking averages from her

N = 128 #total zonal wavenumbers
N2 = 128 #total meridional wavenumbers
Lx = 20. #size of x -- stick to multiples of 10
Ly = 20. #size of y -- stick to multiples of 10

nu = pow( 10., -3. ) #viscous dissipation
km = 0.3 #Ekman friction -- setting in PH88 is 0.3
kt = 0.067 #radiative damping -- value in PH88 is 0.067
bet = 0.15 #beta -- value in PH88 is 0.15
pi = math.pi #always useful

g = 0.04 #leapfrog filter coefficient

#Wavenumbers:
kk = np.fft.fftfreq( N , Lx / float(N) ) #zonal
ll = np.fft.fftfreq( N2 , Ly / float(N2) ) #meridional

x = np.linspace( 0, 2. * pi * Lx, N ) 
y = np.linspace( 0, 2. * pi * Ly, N2 )

#Spectral arrays:
#Only need 3 time-steps
psic_1 = np.zeros( ( ( 3 , N2 , N ) ) ).astype( complex )
psic_2 = np.zeros( ( ( 3 , N2 , N ) ) ).astype( complex )
qc_1 = np.zeros( ( ( 3 , N2, N ) ) ).astype( complex )
qc_2 = np.zeros( ( ( 3 , N2 , N ) ) ).astype( complex )

#Growth rate
gr = np.zeros( ( ( ts - lim, N2 , N  ) ) )
#Streamfunction
psi = np.zeros( ( N, N2 ) )

#######################################################
#  Spectral functions

def ft( psi ):
    """Fourier Transform and keep relevant coefficients"""
    psic = np.fft.fft2( psi )
    return psic 

def ift( psic ):
    """Inverse Fourier Transform"""
    psi = np.fft.ifft2( psic )
    return psi

def ptq(ps1, ps2, ll, kk):
    """Calculate PV"""
    q1 = -(ll[:, np.newaxis] ** 2 + kk[np.newaxis, :] ** 2 ) * ps1 - (ps1 - ps2) / 2. # -(k^2 + l^2) * psi_1 -0.5*(psi_1-psi_2)
    q2 = -(ll[:, np.newaxis] ** 2 + kk[np.newaxis, :] ** 2 ) * ps2 + (ps1 - ps2) / 2. # -(k^2 + l^2) * psi_2 +0.5*(psi_1-psi_2)
    return q1, q2

def qtp(q1_s, q2_s, ll, kk):
	"""Invert PV"""
	psi_bt = -(q1_s + q2_s) / (ll[:, np.newaxis] ** 2 + kk[np.newaxis, :] ** 2) / 2.  # (psi_1 + psi_2)/2
	psi_bc = -(q1_s - q2_s) / (ll[:, np.newaxis] ** 2 + kk[np.newaxis, :] ** 2 + 1. ) / 2.  # (psi_1 - psi_2)/2
	psi_bt[0, 0] = 0.
	psi1 = psi_bt + psi_bc
	psi2 = psi_bt - psi_bc

	return psi1, psi2

#######################################################
#  Time-stepping functions


def lterm(lay, kk, ll, qc, psi, opsi, upsi):
    """"
    Calculate linear terms
    Here follows Panetta and Held (1993). Upper layer is:
    -dq_1/dx - (\beta + 0.5) * d\psi_1/dx + \kappa_t (\psi_1 - \psi_2)
    Lower layer is:
    - (\beta - 0.5) * d\psi_1/dx - \kappa_t (\psi_1 - \psi_2)	
    """
    if lay == 1:
         return -1.j * kk[np.newaxis, :] * qc - 1.j * kk[np.newaxis, :] * ( bet + 0.5 ) * psi + kt * (psi - upsi)
    else:
        return  -1.j * kk[np.newaxis, :] * ( bet - 0.5 ) * psi + km * ( kk[np.newaxis, :] **2 + ll[:, np.newaxis] ** 2) * opsi + kt * (psi - upsi)



def calc_nl( psi, qc ):
    	""""Calculate non-linear terms, with Orszag 3/2 de-aliasing"""

	N, N2 = np.shape( psi )
	ex = N * 3 / 2
	ex2 = N2 * 3 / 2

	temp1 = np.zeros( ( ex, ex2 ) ).astype( complex )
    	temp2 = np.zeros( ( ex, ex2 ) ).astype( complex )
	temp4 = np.zeros( ( N, N2 ) ).astype( complex )	#Final array

	#Pad values:
	temp1[:N/2, :N2 / 2] = psi[:N/2, :N2 / 2]
	temp1[ex-N/2:, :N2 / 2] = psi[N/2:, :N2/ 2]
	temp1[:N/2, ex2 - N2 / 2:] = psi[:N/2, N2/ 2:]
	temp1[ex-N/2:, ex2 - N2 / 2:] = psi[N/2:, N2/ 2:]

	temp2[:N/2, :N2 / 2] = qc[:N/2, :N2 / 2]
	temp2[ex-N/2:, :N2 / 2] = qc[N/2:, :N2/ 2]
	temp2[:N/2, ex2 - N2 / 2:] = qc[:N/2, N2/ 2:]
	temp2[ex-N/2:, ex2 - N2 / 2:] = qc[N/2:, N2/ 2:]

	#Fourier transform product, normalize, and filter:
	temp3 = np.fft.fft2( np.fft.ifft2( temp1 ) * np.fft.ifft2( temp2 ) ) * (3. / 2.) ** 2
	temp4[:N/2, :N2 / 2] = temp3[:N/2, :N2 / 2]
	temp4[:N/2, N2 / 2:] = temp3[:N/2, ex2 - N2 / 2:]
	temp4[N/2:, :N2 / 2] = temp3[ex-N/2:, :N2 / 2]
	temp4[N/2:, N2 / 2:] = temp3[ex-N/2:, ex2 - N2 / 2:]

	return temp4

def nlterm(kk, ll, psi, qc):
   	""""Calculate Jacobian"""

	dpsi_dx = 1.j * kk[np.newaxis, :] * psi
	dpsi_dy = 1.j * ll[:, np.newaxis] * psi

	dqc_dx = 1.j * kk[np.newaxis, :] * qc
	dqc_dy = 1.j * ll[:, np.newaxis] * qc 

	NL1 = calc_nl( dpsi_dx, dqc_dy )
	NL2 = calc_nl( dpsi_dy, dqc_dx )

	return  NL1 - NL2

def fs(ovar, rhs, det, kk, ll):
    """Forward Step: q^t-1 / ( 1 + 2. * dt * nu * (k^4 + l^4 ) ) + RHS"""
    mult = det / ( 1. + det * nu * (kk[np.newaxis, :] ** 4 + ll[:, np.newaxis] ** 4) )
    return mult * (ovar / det + rhs)

def lf(oovar, rhs, det, kk, ll):
    """Leap frog timestepping: q^t-1 / ( 1 + 2. * dt * nu * (k^4 + l^4 ) ) + RHS"""
    mult = 2. * det / ( 1. + 2. * det * nu * (kk[np.newaxis, :] ** 4 + ll[:, np.newaxis] ** 4) )
    return mult * (oovar / det / 2. + rhs)

def filt(var, ovar, nvar):
	"""Leapfrog filtering"""
	return var + g * (ovar - 2. * var + nvar )

#######################################################
#  Initial conditions:


psic_1[0] = np.fft.fft2([ [ random() * .00001  for i in range(N) ] for j in range(N2) ])
psic_2[0] = np.fft.fft2([ [ random() * .00001  for i in range(N) ] for j in range(N2) ])


#Transfer values:
psic_1[ 1 , : , : ] = psic_1[ 0 , : , : ]
psic_2[ 1 , : , : ] = psic_2[ 0 , : , : ]

psic_1[:, 0, 0] = 0.
psic_2[:, 0, 0] = 0.

#Calculate initial PV
qc_1[0], qc_2[0] = ptq(psic_1[0], psic_2[0], ll, kk)
qc_1[1], qc_2[1] = ptq(psic_1[1], psic_2[1], ll, kk)


#######################################################
#  Scatter: 
#  Note that the model 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

print "*********************"
print "Number of processes: ", size
print "Wavenumbers in each process: ", N / size
print "*********************"

if rank == 0:
	p_psi_1 = np.array_split(psic_1, size, axis=1) #Split along y axies
	p_psi_2 = np.array_split(psic_2, size, axis=1)
	p_q_1 = np.array_split(qc_1, size, axis=1)
	p_q_2 = np.array_split(qc_2, size, axis=1)
	p_ll = np.array_split(ll, size)
	p_gr = np.array_split(gr, size, axis = 1)
else:
	p_psi_1 = None
	p_psi_2 = None
	p_q_1 = None
	p_q_2 = None
	p_ll = None	
	p_gr = None

s_psi_1 = comm.scatter(p_psi_1, root=0)
s_psi_2 = comm.scatter(p_psi_2, root=0)
s_q_1 = comm.scatter(p_q_1, root=0)
s_q_2 = comm.scatter(p_q_2, root=0)
s_ll = comm.scatter(p_ll, root=0)
s_gr = comm.scatter(p_gr, root=0)


#######################################################
#  Main time-stepping loop

print "Timestep:", 0

forc1 = np.zeros( (N / size, N2 ) ).astype(complex)
forc2 = np.zeros( (N / size, N2 ) ).astype(complex)
nl1 = np.zeros( (N / size, N2 ) ).astype(complex)
nl2 = np.zeros( (N / size, N2 ) ).astype(complex)

#Timestepping:
for i in range( 1, ts ):

	if i % 10 == 0:
        	print "Timestep:", i

        if opt > 1:
        	nl1[:, :] = nlterm(kk, s_ll, s_psi_1[1, :, :], s_q_1[1, :, :])
        	nl2[:, :] = nlterm(kk, s_ll, s_psi_2[1, :, :], s_q_2[1, :, :])

        if opt != 2:

        	forc1[:, :] = lterm(1, kk, s_ll, s_q_1[1, :, :], s_psi_1[1, :, :], s_psi_1[0, :, :], s_psi_2[1, :, :])
       		forc2[:, :] = lterm(2, kk, s_ll, s_q_2[1, :, :], s_psi_2[1, :, :], s_psi_2[0, :, :], s_psi_1[1, :, :])

        rhs1 = nl1[:] + forc1[:]
        rhs2 = nl2[:] + forc2[:]

        if i == 1:
		#Forward step
        	s_q_1[2, :] = fs(s_q_1[1, :, :], rhs1[:], dt, kk, s_ll)
        	s_q_2[2, :] = fs(s_q_2[1, :, :], rhs2[:], dt, kk, s_ll)
        else:
		#Leapfrog step
        	s_q_1[2, :, :] = lf(s_q_1[0, :, :], rhs1[:], dt, kk, s_ll)
        	s_q_2[2, :, :] = lf(s_q_2[0, :, :], rhs2[:], dt, kk, s_ll)

        if i > 1:
		#Leapfrog filter
                s_q_1[1, :] = filt(s_q_1[1, :], s_q_1[0, :], s_q_1[2, :])
                s_q_2[1, :] = filt(s_q_2[1, :], s_q_2[0, :], s_q_2[2, :])

   	#Invert:
   	s_psi_1[0], s_psi_2[0] = qtp(s_q_1[1], s_q_2[1], s_ll, kk )
   	s_psi_1[1], s_psi_2[1] = qtp(s_q_1[2], s_q_2[2] , s_ll, kk)

	if i > lim:
		#Calculate growth rates
		s_gr[i - lim, :] =  np.log( abs( s_psi_1[1, :N / size , :N] ) / abs( s_psi_1[0, :N / size , :N] ) ) / dt 

	#Transfer values:
	s_q_1[0, :, :] = s_q_1[1, :, :]
	s_q_2[0, :, :] = s_q_2[1, :, :]
	s_q_1[1, :, :] = s_q_1[2, :, :]
	s_q_2[1, :, :] = s_q_2[2, :, :]

comm.Barrier() #Wait for everyone to catch up, then gather

n_gr = comm.gather(s_gr,root=0)
n_psi = comm.gather(s_psi_1,root=0)

if rank == 0:
	#Plot growth rates and streamfunction at final time-step
	n_gr = np.swapaxes( n_gr, 0, 1 )	
  	n_gr2 = np.reshape( n_gr, ( ( ( ts - lim, N2 , N ) ) ) )

	fig = plt.figure( figsize = (10, 10) )
	plt.subplots_adjust( left = 0.08, right = 0.9, bottom = 0.05, top = 0.95, hspace = 0.35 )

	ax = plt.subplot(2, 1, 1)
	plt.title( "Growth Rates", fontsize = 14)

	levs = np.arange(0., 0.22, 0.02)
	plt.contourf( kk[:N/2], ll[:N2/2], np.mean( n_gr2[:, :N2/2, :N/2], axis = 0 ), levs, cmap = plt.cm.Reds )
	cb = plt.colorbar()

	plt.xlabel("Zonal Wavenumber", fontsize = 14)
	plt.ylabel("Meridional Wavenumber", fontsize = 14)
	ax.tick_params(axis = 'x', which = 'both', direction = 'out', top = 'off')
	ax.tick_params(axis = 'y', which = 'both', direction = 'out', right = 'off')

	n_psi = np.swapaxes( n_psi, 0, 1 )	
  	n_psi = np.reshape( n_psi, ( ( ( 3, N2 , N ) ) ) )
	real_psi = np.fft.ifft2( n_psi[1] )

	ax = plt.subplot(2, 1, 2)
	plt.title("Upper-level Streamfunction at time: " + str(ts * dt), fontsize = 14)

	levs = np.arange(-0.003, 0.0033, 0.0003)
	plt.contourf( x, y, real_psi, levs, cmap = plt.cm.seismic )
	cb = plt.colorbar()

	plt.xlabel("X", fontsize = 14)
	plt.ylabel("Y", fontsize = 14)
	ax.tick_params(axis = 'x', which = 'both', direction = 'out', top = 'off')
	ax.tick_params(axis = 'y', which = 'both', direction = 'out', right = 'off')

	plt.savefig("Growth_rates_streamfunction.png")
	plt.show()
		









