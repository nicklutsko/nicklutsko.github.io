""""
Nicholas Lutsko -- EAPS department, MIT

Functions for calculating eddy flux co-spectra. Script follows technique of Hayashi (1971) (see also Randel and Held (1991)) and calculates spectra at a specific height.

Includes functions to calculate space-time cross-spectra and phase-speed cross-spectrum.

Updated May 30th 2018 -- fixed bug pointed out by Ben Toms

Updated March 8th 2019 -- fixed documentation errors pointed out by Neil Lewis
"""
import numpy as np
import scipy.signal as ss
import scipy.interpolate as si


def calc_spacetime_cross_spec( a, b, Fs = 1., smooth = 1, width = 4., windows = 8, NFFT = 256 ):
	"""
	Calculate space-time co-spectra, following method of Hayashi (1971)

	Input:
	  a - variable 1, dimensions = (time, lon)
	  b - variable 2, dimensions = (time, lon)
	  Fs - sampling frequency
	  smooth - 1 = apply Gaussian smoothing
          width - width of Gaussian smoothing
          windows - number of windows in cross-spectra calculations
          NFFT - length of FFT in cross-spectra calculations

	Output:
	  K_p - spectra for positive frequencies
	  K_n - spectra for negative frequencies
	  lon_freqs - inverse wavenumbers
	  om - frequencies 
	  K_combine - spectra for all frequencies 


	Note: the calculations will fail if the time dimension is larger than windows * NFFT (2048      	currently)
	"""
	t, l = np.shape( a )
	lf = l / 2 + 1
	tf = 129
	lon_freq = 2. * np.pi * np.linspace(0., 0.5, lf)
	
	#Calculate spatial ffts
	Fa = np.fft.fft( a, axis = 1 )
	Fb = np.fft.fft( b, axis = 1 )

	CFa = Fa[:, :l/2 + 1].real
	SFa = -Fa[:, :l/2 + 1].imag
	CFb = Fb[:, :l/2 + 1].real
	SFb = -Fb[:, :l/2 + 1].imag

	K_p = np.zeros( ( tf, lf ) )
	K_n = np.zeros( ( tf, lf ) )
	
	#Cross-spectra
	for i in range( lf ):
		window = np.hamming( len(CFa[:, i]) / 8)
		om, csd_CaCb = ss.csd( CFa[:, i], CFb[:, i], fs = Fs * 2. * np.pi, window = window, nperseg = len(CFa[:, i]) / windows, nfft = NFT )
		om, csd_SaSb = ss.csd( SFa[:, i], SFb[:, i], fs = Fs * 2. * np.pi, window = window, nperseg = len(CFa[:, i]) / windows, nfft = NFT )
		om, csd_CaSb = ss.csd( CFa[:, i], SFb[:, i], fs = Fs * 2. * np.pi, window = window, nperseg = len(CFa[:, i]) / windows, nfft = NFT )
		om, csd_SaCb = ss.csd( SFa[:, i], CFb[:, i], fs = Fs * 2. * np.pi, window = window, nperseg = len(CFa[:, i]) / windows, nfft = NFT)

		K_p[:, i] = csd_CaCb.real + csd_SaSb.real + csd_CaSb.imag - csd_SaCb.imag
		K_n[:, i] = csd_CaCb.real + csd_SaSb.real - csd_CaSb.imag + csd_SaCb.imag

	#Combine
	K_combine = np.zeros( ( tf * 2, lf ) )
	K_combine[:tf, :] = K_n[::-1, :]
	K_combine[tf:, :] = K_p[:, :]

	#Apply smoothing
	if smooth == 1.:
		f_size = len(K_p[:, 0])
		sigma = 1. / width / np.pi * tf
		x = np.linspace( -tf / 2, tf / 2., tf )
		gauss_filter = np.exp( -x ** 2 / (2. * sigma ** 2 ) )
		gauss_filter /= sum( gauss_filter )
 		for i in range( lf ):
			K_combine[:, i] = np.convolve( K_combine[:, i], gauss_filter, 'same' )

	#Take out positive and negative parts
	K_n = K_combine[:tf, :]
	K_p = K_combine[tf:, :]
	K_n = K_n[::-1, :]

	return K_p, K_n, lon_freq, om 


def calc_phase_speed_spec( P_p, P_n, f_lon, om, lon_unit, time_unit, nps, i1 = 1, i2 = 50 ):
	"""
	Calculate space-time co-spectra, following method of Hayashi (1971)

	Input:
	  P_p - spectra for positive phase speeds
	  P_n - spectra for negative phase speeds
	  f_lon - inverse wavenumbers
	  om - frequencies 
	  lon_unit - spacing of longitude
	  time_unit - sampling interval
	  nps - size of phase speed grid
	  i1 - lowest wave number to sum over
          i2 - highest wave number to sum over
	
	Output:
	  P_cp - spectra for positive phase speeds
	  P_cn - spectra for negative phase speeds
	  C * lon_unit / time_unit - phase speeds
	"""
	if i2 < i1:
		print "WARNING: highest wavenumber smaller than lowest wavenumber"

	#Make non-dimensional phase speed grid
	j = len( f_lon )
	t = len( om )
	C = np.linspace( om[1] / f_lon[j / 6], om[t - 1] / f_lon[1], nps )

	P_cp = np.zeros( nps )
	P_cn = np.zeros( nps )

	#Interpolate
	for i in range( i1+4, i2 ):
		f1 = si.interp1d(om, P_p[:, i], 'linear' )
		f2 = si.interp1d(om, P_n[:, i], 'linear' )

		#interp1d doesn't handle requested points outside data range well, so just zero out these points
		k = -1
		for j in range( len(C) ):
			if C[j] * f_lon[i] > max(om):
				k = j
				break
		if k == -1:
			k = len( C )			
		ad1 = np.zeros( 100 )
		ad1[:k] =  f1( C[:k] * f_lon[i] )
		ad2 = np.zeros( 100 )
		ad2[:k] =  f2( C[:k] * f_lon[i] )

		#Interpolate
		P_cp = P_cp + i * ad1
		P_cn = P_cn + i * ad2

	return P_cp, P_cn, C * lon_unit / time_unit


def calc_co_spectra( x, y, dx, dt, nps = 100 ):
	"""
	Calculate eddy phase speed co-spectra, following method of Hayashi (1971)

	Input:
	  x - variable 1, dimensions = (time, lat, lon)
	  y - variable 2, dimensions = (time, lat, lon)
	  dx - spacing of longitude
	  dt - sampling frequency
	  nps - grid of phase speeds

	Output:
	  p_spec - the spectra
	  ncps - phase speeds
	"""
	if x.ndim != 3:
		print "WARNING: Dimensions of x != 3"
	if y.ndim != 3:
		print "WARNING: Dimensions of y != 3"

	t, l, j = np.shape( x )
	x -= np.mean( x, axis = 2 )[:, :, np.newaxis]
	y -= np.mean( y, axis = 2 )[:, :, np.newaxis]

	p_spec = np.zeros( ( l, 2 * nps ) ) #array to hold spectra

	#Cycle through latitudes
	for i in range( l ):
		print "Doing: ", i
		#First calculate space - time cross-spectra
		K_p, K_n, lon_freq, om = calc_spacetime_cross_spec( x[:, i, :], y[:, i, :], Fs = dt )
		#Convert to phase speed spectra
		P_Cp, P_Cn, cp = calc_phase_speed_spec(K_p, K_n, lon_freq, om, dx, dt, nps, 1, nps / 2 );
		
		p_spec[i, :nps] = P_Cn[::-1] #negative phase speeds
		p_spec[i, nps:] = P_Cp[:] #positive phase speeds

	ncps = np.zeros( 2 * nps ) #full array of phase speeds 
	ncps[:100] = -1. * cp[::-1] 
	ncps[100:] = cp[:] 

	return p_spec, ncps



