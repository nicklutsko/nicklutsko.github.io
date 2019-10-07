""""
Nicholas Lutsko -- EAPS department, MIT

Functions for calculating eddy flux co-spectra. Script follows technique of Hayashi (1971) (see also Randel and Held (1991)) and calculates spectra at a specific height.

Includes functions to calculate space-time cross-spectra and phase-speed cross-spectrum.

Updated May 30th 2018 -- fixed bug identified by Ben Toms

Updated March 14th 2019 -- fixed several bugs identified by Neil Lewis

Tested using Python 2.7.12
"""
import numpy as np
import scipy.signal as ss
import scipy.interpolate as si


def calc_spacetime_cross_spec( a, b, ts = 1., smooth = 1, width = 15., NFFT = 256 ):
	"""
	Calculate space-time co-spectra, following method of Hayashi (1971)

	Input:
	  a - variable 1, dimensions = (time, space)
	  b - variable 2, dimensions = (time, space)
	  dx - x-grid spacing (unit = space)
	  ts - sampling interval (unit = time)
	  smooth - 1 = apply Gaussian smoothing
          width - width of Gaussian smoothing
          NFFT - length of FFT in cross-spectra calculations, sets the size of the 

	Output:
	  K_p - spectra for positive frequencies
	  K_n - spectra for negative frequencies
	  lon_freqs - wavenumbers
	  om - frequencies 
	"""
	t, l = np.shape( a )
	lf = l / 2 

	#Calculate spatial ffts. 
	Fa = np.fft.fft( a, axis = 1 ) / float( l  ) #normalize as in Randel and Held 1991
	Fb = np.fft.fft( b, axis = 1 ) / float( l  ) #normalize as in Randel and Held 1991

	#Only keep positive wavenumbers
	lon_freq = np.fft.fftfreq( l, d = dx )[:lf] #=n / a cos\phi in Randel Held 

	CFa = Fa[:, :lf].real
	SFa = Fa[:, :lf].imag
	CFb = Fb[:, :lf].real
	SFb = Fb[:, :lf].imag

	tf = NFFT / 2 + 1

	#K_n,w arrays
	K_p = np.zeros( ( tf, lf ) )
	K_n = np.zeros( ( tf, lf ) )
	
	#Cross-spectra
	for i in range( lf ):
		window = np.hamming( NFFT )
		csd_CaCb, om = mm.csd( CFa[:, i], CFb[:, i], Fs = 1. / ts, NFFT = NFFT, scale_by_freq = True, window=mm.window_hanning)
		csd_SaSb, om = mm.csd( SFa[:, i], SFb[:, i], Fs = 1. / ts, NFFT = NFFT, scale_by_freq = True, window=mm.window_hanning) 
		csd_CaSb, om = mm.csd( CFa[:, i], SFb[:, i], Fs = 1. / ts, NFFT = NFFT, scale_by_freq = True, window=mm.window_hanning) 
		csd_SaCb, om = mm.csd( SFa[:, i], CFb[:, i], Fs = 1. / ts, NFFT = NFFT, scale_by_freq = True, window=mm.window_hanning)
		K_p[:, i] = csd_CaCb.real + csd_SaSb.real + csd_CaSb.imag - csd_SaCb.imag
		K_n[:, i] = csd_CaCb.real + csd_SaSb.real - csd_CaSb.imag + csd_SaCb.imag
		#Don't need factor 4 from Hayashi eq4.11, since Fourier co-efficients are 1/2 as large due to only retaining positive wavenumbers

	#Combine
	K_combine = np.zeros( ( tf * 2, lf ) ) 
	K_combine[:tf, :] = K_n[::-1, :]   #for the convolution
	K_combine[tf:, :] = K_p[:, :]  


	if smooth == 1.:
		x = np.linspace( -tf / 2, tf / 2., tf )
		gauss_filter = np.exp( -x ** 2 / (2. * width ** 2 ) )
		gauss_filter /= sum( gauss_filter )
 		for i in range( lf ):
			K_combine[:, i] = np.convolve( K_combine[:, i], gauss_filter, 'same' )

	#Take out positive and negative parts
	K_n = K_combine[:tf, :]
	K_p = K_combine[tf:, :]
	K_n = K_n[::-1, :]

	return K_p , K_n, lon_freq, om 

def calPhaseSpeedSpectrum( P_p, P_n, f_lon, om, cmax, nps, i1 = 1, i2 = 50 ):
	"""
	Calculate space-time co-spectra, following method of Hayashi (1971)

	Input:
	  P_p - spectra for positive phase speeds
	  P_n - spectra for negative phase speeds
	  f_lon - wavenumbers
	  om - frequencies 
	  cmax - maximum phase speed
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

	j = len( f_lon )
	t = len( om )

	#Make phase speed grid	
	C = np.linspace(0., cmax, nps)

	#K_n,c arrays
	P_cp = np.zeros( ( nps, j ) )
	P_cn = np.zeros( ( nps, j ) )

	#Interpolate
	for i in range( i1, i2 ):
		#Make interpolation functions c = omega / k
		f1 = si.interp1d(om / f_lon[i], P_p[:, i], 'linear' )
		f2 = si.interp1d(om / f_lon[i], P_n[:, i], 'linear' )

		#interp1d doesn't handle requested points outside data range well, so just zero out these points
		k = -1
		for j in range( len(C) ):
			if C[j] > max(om) / f_lon[i]:
				k = j
				break
		if k == -1:
			k = len( C )	
		
		ad1 = np.zeros( nps )
		ad1[:k] =  f1( C[:k]  )
		ad2 = np.zeros( nps )
		ad2[:k] =  f2( C[:k] )

		#Interpolate
		P_cp[:, i] = ad1 * f_lon[i] 
		P_cn[:, i] = ad2 * f_lon[i] 

 	#Sum over all wavenumbers
	return np.sum(P_cp, axis = 1), np.sum(P_cn, axis = 1), C

def calc_co_spectra( x, y, dx, lat, dt, cmax = 50, nps = 50 ):
	"""
	Calculate eddy phase speed co-spectra, following method of Hayashi (1974)

	Input:
	  x - variable 1, dimensions = (time, lat, lon)
	  y - variable 2, dimensions = (time, lat, lon)
	  dx - spacing of spatial points (unit = m)
	  lat - latitudes -> note that if working in spherical co-ordinates dx must be scaled by 
		a * cos(lat)
	  dt - sampling interval (unit = s)
	  cmax - maximum phase speed 
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
		#Calculate space - time cross-spectra
		K_p, K_n, lon_freq, om = spaceTimeCrossSpec( x[:, i, :], y[:, i, :], dx = dx, ts = dt )
		#Convert to phase speed spectra
		P_Cp, P_Cn, cp = calPhaseSpeedSpectrum(K_p, K_n, lon_freq, om, cmax, nps, 1, nps / 2 );
		
		p_spec[i, :nps] = P_Cn[::-1] #negative phase speeds
		p_spec[i, nps:] = P_Cp[:] #positive phase speeds

	ncps = np.zeros( 2 * nps ) #full array of phase speeds 
	ncps[:100] = -1. * cp[::-1] 
	ncps[100:] = cp[:] 

	return p_spec, ncps



