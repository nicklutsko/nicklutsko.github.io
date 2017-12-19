import numpy as np
import spectrum

def adaptive_weights(x, Pk, nx, V ):

	sig2 = np.matrix(x) * np.matrix(x).H / nx # power
	P = ( Pk[0, :] + Pk[1, :] ) / 2 #initial spectrum estimate
        P1 = np.zeros( nx )
	tol = .0005 * sig2 / nx # usually within tolerance in about three iterations, see equations from [2] (P&W pp 368-370).   
   	a = np.array( sig2 * (1. - V) )
  	while sum( abs( P - P1 ) / nx) > tol:  
		b = P[:, np.newaxis] / ( P[:, np.newaxis] * V[np.newaxis, :] + a[np.newaxis, :] ) # weights
	        wk = (b ** 2) * V[np.newaxis, :] # new spectral estimate
		wk = np.swapaxes( wk, 1, 2 )
	        P1 = sum( wk[0, :, :] * Pk ) / np.sum( wk[0, :, :], axis = 0 ) 	
	        # swap P and P1
		Ptemp = P1[:]
	        P1 = P
	        P = Ptemp

	return P, b, wk


def multi_taper_ps( x, nfft, dt = 1, nw = 3 ):
	"""
	Based on script available at Peter Huybers' website:
	http://www.people.fas.harvard.edu/~phuybers/Mfiles/index.html

	Inputs:
	  x      - Input data vector.
	  nfft   - Number of frequencies to evaluate P at, set to
		   length(x) for the two-sided transform. 
	  dt     - Sampling interval, default is 1.
	  nw     - Time bandwidth product, acceptable values are
		   0:.5:length(x)/2-1, default is 3.  2*nw-1 dpss tapers
		   are applied except if nw=0 a boxcar window is applied 
		   and if nw=.5 (or 1) a single dpss taper is applied.

	Outputs:
	  P      - Power spectrum computed via the multi-taper method.
	  s      - Frequency vector.
	  ci     - 95% confidence intervals. Note that both the degrees of freedom
		   calculated by pmtm.m and chi2conf.m, which pmtm.m calls, are
		   incorrect.  Here a quick approximation method is used to
		   determine the chi-squared 95% confidence limits for v degrees
		   of freedom.  The degrees of freedom are close to but no larger
		   than (2*nw-1)*2; if the degrees of freedom are greater than
		   roughly 30, the chi-squared distribution is close to Gaussian.

		   The vertical ticks at the top of the plot indicate the size of
		   the full band-width.  The distance between ticks would remain
		   fixed in a linear plot.  For an accurate spectral estimate,
		   the true spectra should not vary abruptly on scales less than
		   the full-bandwidth.

	"""

	nx = len(x)
	k = min( round(2 * nw), nx )
	k = int( max( k - 1, 1) ) #number of windows
	w = float(nw) / float(dt*nx) #half-bandwidth of the dpss
	s = np.arange(0., 1. / dt, 1. / nfft / dt )

	#Compute the discrete prolate spheroidal sequences
	E, V = spectrum.dpss( nx, nw, k )

	#Compute the windowed DFTs.
	#if nx<=nfft
	Pk = np.zeros( ( k, nx ) )
	for i in range( k ):
		fx = np.fft.fft( E[:, i] * x[:], nfft)
   		Pk[i, :] = abs( np.fft.fft( E[:, i] * x[:], nfft) ) ** 2

	#else  #compute DFT on nfft evenly spaced samples around unit circle:
   	#	Pk=abs(czt(E(:,1:k).*x(:,ones(1,k)),nfft)).^2; 
	####python doesn't have czt function. Can find scripts online, but for now just leave it

	#Iteration to determine adaptive weights:    
  	if k > 1:
   		P, b, wk = adaptive_weights( x, Pk, nfft, V )
   		#Determine equivalent degrees of freedom, see p.  of Percival and Walden 1993.
   		v = (2. * np.sum( (b ** 2) * V[np.newaxis, :], axis = 2 ) ** 2 ) / (np.sum( (b ** 4) * ( V[np.newaxis, :] ** 2 ), axis = 2 ) )
	else: #simply the periodogram;
	     P = Pk
	     v = 2.* np.ones( nfft )

	#cut records
	P = P[:(nfft + 1) / 2 + 1]
	s = s[:(nfft + 1) / 2 + 1]
	v = v[0, :(nfft + 1) / 2 + 1]

	#Chi-squared 95% confidence interval
	#approximation from Chambers et al 1983; see Percival and Walden p.256, 1993
	ci = np.zeros( ( 2, len( v ) ) )
	ci[0, :] = 1. / (1. - 2. / (9. * v ) - 1.96 * np.sqrt( 2. / ( 9 * v ) ) ) ** 3
	ci[1, :] = 1. / (1. - 2. / (9. * v ) + 1.96 * np.sqrt( 2. / ( 9 * v ) ) ) ** 3
	
	return P, s, ci


def multi_taper_coh( x, y, dt = 1, nw = 8, qbias = 0, confn = 0 ):
	"""
	Based on script available at Peter Huybers' website:
	http://www.people.fas.harvard.edu/~phuybers/Mfiles/index.html

	Inputs:
	   x     - Input data vector 1.  
	   y     - Input data vector 2.  
	   dt    - Sampling interval (default 1) 
	   nw    - Number of windows to use (default 8) 
	   qbias - Correct coherence estimate for bias (yes, 1)  (no, 0, default).
	   confn - Number of iterations to use in estimating phase uncertainty using a Monte Carlo method. (default 0)

	Outputs:
	   s       - frequency
	   c       - coherence
	   ph      - phase
	   ci      - 95% coherence confidence level
	   phi     - 95% phase confidence interval, bias correct (add and subtract phi from ph).

	##############################
	##############################
	Note: the coherence bias and confidence intervals are difficult to calculate - Peter Huybers includes a script which 	     estimates these that takes about an hour to run on a 2Ghz machine. For now, don't calculate the bias and confidence 		intervals.
	##############################
	##############################

	"""

	if nw < 1.5:
		print "WARNING: nw must be >= 1.5"
	
	print "Number of windows: ", nw
	if qbias == 1:
		print "Bias correction: On"
	else:
		print "Bias correction: Off"
	print "Confidence iterations: ", confn

	x -= np.mean( x )
	y -= np.mean( y )
	
	if len( x ) != len( y ):
		print "WARNING: length x != length y"

	#define some parameters
	nx = len(x);
	k = min( round(2 * nw), nx )
	k = int( max( k - 1, 1) ) #number of windows
	s = np.arange(0., 1. / dt, 1. / nx / dt )
	pls = np.arange(2, (nx + 1) / 2 + 1 )
	v = (2. * nw - 1) #approximate degrees of freedom

	if len(y)%2 == 1:
		pls = pls[:len(pls) - 1]

	#Compute the discrete prolate spheroidal sequences
	E, V = spectrum.dpss( nx, nw, k )

	#Compute the windowed DFTs.
	fkx = np.zeros( ( k, nx ) ).astype(complex)
	fky = np.zeros( ( k, nx ) ).astype(complex)
	for i in range( k ):
   		fkx[i, :] = np.fft.fft( E[:, i] * x[:], nx)
   		fky[i, :] = np.fft.fft( E[:, i] * y[:], nx)
	Pkx = abs( fkx ) ** 2
	Pky = abs( fky ) ** 2

	#Iteration to determine adaptive weights:    
  	for i in range( 2 ):
		if i == 0:
			P, b, wk = adaptive_weights( x, Pkx, nx, V ) 	
			fkx = np.sqrt( k ) * np.sqrt( wk[0] ) * fkx / (np.sum( np.sqrt( wk[0] ), axis = 0 ) )[np.newaxis, :]
			Fx = P #Power density spectral estimate of x
		elif i == 1:
			P, b, wk = adaptive_weights( y, Pky, nx, V ) 
			fky = np.sqrt( k ) * np.sqrt( wk[0] ) * fky / (np.sum( np.sqrt( wk[0] ), axis = 0 ) )[np.newaxis, :]
			Fy = P #Power density spectral estimate of y

	#Compute coherence and phase 
	Cxy = np.sum( fkx * np.conj( fky ), axis = 0 )
	Cxy = np.conj( Cxy ) 
	ph = np.angle( Cxy ) * 180. / np.pi
	c = abs( Cxy ) / np.sqrt( np.sum( abs( fkx ) ** 2, axis = 0) * np.sum( abs( fky ) ** 2, axis = 0 ) )

	#cut records
	c = c[1:(nx + 1) / 2 + 1]
	s = s[1:(nx + 1) / 2 + 1]
	ph = ph[1:(nx + 1) / 2 + 1]

	phi = np.zeros( len(pls) ) 
	ci = np.zeros( len( c ) )

	return s, c, ph, ci, phi












