""""
Nicholas Lutsko -- EAPS Department, MIT

Script to solve 1D moist EBM described in Merlis and Henry (2018), 
originally based on the dry EBM in Wagner and Eisenman (2015).

The P - E data is available at:
http://nicklutsko.github.io/code/MERRA_P_E.dat

Last updated -- April 25th 2019
"""
import numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


###############################
# Model parameters

l = 180 #number of grid-points
sin_lat = np.linspace( 0., 1., l ) #x = sin latitude
dx = sin_lat[1] - sin_lat[0]
lat = np.arcsin( sin_lat ) * 180. / np.pi #latitude

Q = 1360. #solar constant
L = 2.5 * 10. ** 6 #latent heat of vaporization
rh = 0.8 #assume a fixed relative humidity
cp = 1004.6 #heat capacity of air

gamma = 0.482 #for calculating the insolation structure function
P2 = 1. / 2. * ( 3 * sin_lat ** 2 - 1) #second Legendre polynomial
a0 = 0.68 #for calculating co-albedo
a2 = -0.2 #for calculating co-albedo

S = 1. - gamma * P2 #insolation structure function
a = a0 + a2 * P2 #co-albedo

insolation = 1. / 4. * Q * S * a #latitudinal profile of insolation

#Feedback co-efficients:
A = -281.67
B = 1.8

cw = 9.8 #heat capacity of mixed layer
D = 0.3 #diffusivity


###############################
# Model functions

def calc_qs( T ):
	#Calculate saturation mixing ratio

	#first calculate saturation vapor pressure using the August-Roche-Magnus approximation
	qsat = 0.61094 * np.exp( 17.625 * (T - 273.15) / ( (T - 273.15) + 243.04) ) * 1000.
	#convert to mixing ratio
	return 0.622 * qsat / (1000. * 100. - qsat)


def calc_rhs( T, time ):
	#The RHS of the model	

	#Calculate feedback
	feedback = A + B * T 
	
	#Now do diffusivity:
	qs = calc_qs( T ) #calculate saturation mixing ratio
	h =  T + L * rh * qs / cp #calculate mse / cp

	
	diffusion = np.zeros(l) # = D(1 - x^2)d^2h/dx^2 - 2Dxdh/dx
	#use second-order scheme to calculate Laplacian
	for i in range(1, l - 1 ):
		diffusion[i] = (D / dx**2) * (1. - sin_lat[i]**2) * (h[i+1] - 2 * h[i] + h[i-1]) - (D * sin_lat[i] / dx) * (h[i+1] - h[i-1])
	diffusion[0] = D * 2 * (h[1] - h[0]) / dx**2
	diffusion[-1] = -D * 2 * sin_lat[-1] * (h[-1] - h[-2]) / dx

	#Bring everything together and divide by cw
	return (insolation - feedback + diffusion + F) / cw


###############################
# Plotting stuff

# These are the "Tableau 20" colors as RGB.    
cs = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(cs)):    
    r, g, b = cs[i]    
    cs[i] = (r / 255., g / 255., b / 255.)  

def make_axis( ax ):

	ax.tick_params( axis = 'x', which = 'both', bottom="on", top = "off", labelbottom = "on", direction = 'out')                  
	ax.tick_params( axis = 'y', which = 'both', bottom="off", top="off",  labelbottom="off", left="on", right="off", labelleft="on", direction ='out')                                                                                          

	ax.tick_params(length = 6, which = 'major')
	ax.tick_params(length = 4, which = 'minor')

	ax.spines["top"].set_visible(False)    
	ax.spines["right"].set_visible(False)      

	majorLocator = MultipleLocator( 30 )
	majorFormatter = FormatStrFormatter('%d')
	minorLocator = MultipleLocator( 10 )

	ax.xaxis.set_major_locator(majorLocator)
	ax.xaxis.set_major_formatter(majorFormatter)
	ax.xaxis.set_minor_locator(minorLocator)
	plt.xlabel( "Latitude", fontsize = 14)
	plt.xlim([0., 90.])   
                                                             
	return ax


###############################
# Calculations

fig = plt.figure( figsize = (14, 7) )
plt.subplots_adjust(left = 0.07, right = 0.95, bottom = 0.1, top = 0.95, hspace = 0.3, wspace = 0.27)


#Start by plotting insolation profiles

uni = 2. #uniform reduction by 2 Wm-2

ax = plt.subplot(2, 3, 1)
plt.title( "a)", fontsize = 14 )

plt.plot( lat, insolation, color = 'k', linewidth = 2. )

plt.ylabel("Insolation [Wm$^{-2}$]", fontsize = 14)

majorLocator = MultipleLocator( 40 )
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator( 20 )

ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
ax.yaxis.set_minor_locator(minorLocator)

make_axis( ax )

ax = plt.subplot(2, 3, 4)
plt.title( "d)", fontsize = 14 )

plt.plot( lat, -uni * np.ones( l ), color = cs[2], linewidth = 2. )
plt.plot( lat, insolation * .99 - insolation, color = cs[6], linewidth = 2. )

plt.legend(["uniform", "1%"], frameon = False, loc = "upper left")

plt.ylabel("$\Delta$ Insolation [Wm$^{-2}$]", fontsize = 14)

majorLocator = MultipleLocator( 1 )
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator( 0.5 )

ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
ax.yaxis.set_minor_locator(minorLocator)

make_axis( ax )

#Now do calculations

from scipy.integrate import odeint
Ti = np.ones( l ) * 280. #initial guess
time = np.linspace(0., 10., 1000) 

F = 0 #Forcing
sol = odeint(calc_rhs, Ti, time) # solve
t1 = sol[-1] #keep profile at last time-step

ax = plt.subplot(2, 3, 2)
plt.title( "b)", fontsize = 14 )

plt.plot( lat, t1, color = 'k', linewidth = 2. )

plt.ylabel("$T$ [K]", fontsize = 14)

majorLocator = MultipleLocator( 20 )
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator( 10 )

ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
ax.yaxis.set_minor_locator(minorLocator)

make_axis( ax )

#Do perturbations
F = 4. #forcing

sol = odeint(calc_rhs, Ti, time) #GW
t2 = sol[-1]

insolation -= uni #uniform reduction in insolation
sol = odeint(calc_rhs, Ti, time) 
t3 = sol[-1]

insolation = (insolation + uni) * .99 #reduce insolation by 1%
sol = odeint(calc_rhs, Ti, time)
t4 = sol[-1]

#Plot
ax = plt.subplot(2, 3, 5)
plt.title( "e)", fontsize = 14 )

plt.plot( lat, t2 - t1, color = cs[0], linewidth = 2. )

plt.plot( lat, t3 - t1, color = cs[2], linewidth = 2. )

plt.plot( lat, t4 - t1, color = cs[6], linewidth = 2. )

plt.legend(["GW", "uniform", "1%"], frameon = False, loc = "upper left")

plt.ylabel("$\Delta T$ [K]", fontsize = 14)

majorLocator = MultipleLocator( 1 )
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator( 0.5 )

ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
ax.yaxis.set_minor_locator(minorLocator)

make_axis( ax )

#P - E

p_e = np.load("MERRA_P_E.dat")
p_e = p_e[len(p_e) / 2:] #only retain NH
lat2 = np.linspace(0., 90., len(p_e)) #MERRA has uniform grid-spacing

ax = plt.subplot(2, 3, 3)
plt.title( "c)", fontsize = 14 )

plt.plot( lat2, p_e, color = 'k', linewidth = 2. )

plt.ylabel("P - E [mm day$^{-1}$]", fontsize = 14)

majorLocator = MultipleLocator( 1 )
majorFormatter = FormatStrFormatter('%d')
minorLocator = MultipleLocator( 0.5 )

ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
ax.yaxis.set_minor_locator(minorLocator)

make_axis( ax )

#Interpolate to model grid so can compute responses
from scipy.interpolate import interp1d
f = interp1d( lat2, p_e )
np_e = f(lat)

alpha = 0.07 #7%K-1 increase

ax = plt.subplot(2, 3, 6)
plt.title( "f)", fontsize = 14 )

plt.plot( lat, alpha * (t2 - t1) * np_e, color = cs[0], linewidth = 2. )
plt.plot( lat, alpha * (t3 - t1) * np_e, color = cs[2], linewidth = 2. )
plt.plot( lat, alpha * (t4 - t1) * np_e, color = cs[6], linewidth = 2. )


plt.ylabel("$\Delta$ (P - E) [mm day$^{-1}$]", fontsize = 14)

majorLocator = MultipleLocator( .1 )
majorFormatter = FormatStrFormatter('%0.1f')
minorLocator = MultipleLocator( 0.05 )

ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_major_formatter(majorFormatter)
ax.yaxis.set_minor_locator(minorLocator)

make_axis( ax )


#plt.savefig("moist_EBM_geoengineering.png")
plt.show()







