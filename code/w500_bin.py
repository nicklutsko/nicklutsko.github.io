""""
Nicholas Lutsko -- EAPS department, MIT

Function for binning data by \omega_500 velocities, as described by Bony et al. (2004) and others.

Right now function bins nine variables, but can easily be modified by changes the keys.

Last updated -- May 22nd 2018
"""

import numpy as np
import pandas as pd

def binned_data( data, bins, k = 1 ):
	"""
	Bin data according to \omega_500 velocities

	INPUT:
	data = input data has dimensions ( ( ( ( number of variables, time, x, y ) ) ) ). Code is written assuming data[0] contains the \omega_500 velocities
	bins = edges of bins, in hPa / day
	k = time-averaging parameter. E.g k = 12 results in annual-mean data

	OUTPUT:
	bin_dat = binned data
	pdf_wap = time-series of histogram

	"""
	nv = len(data)	#number of variables to bin
	nb = len( bins ) - 1 #number of bins
	d1, d2, d3 = np.shape( data[0] )

	y = d1 / k #length of time of binned data

	bin_dat = np.zeros( ( ( nv, y, nb) ) ) #final binned data
	pdf_wap = np.zeros( ( y, nb ) ) #pdf of w velocities

	#Now loop over each time point and bin
	for i in range( y ):
		if i % 100 == 0:
			print "Doing: ", i

		#Reshape and convert to DataFrame object
		ndat = np.reshape( data[:, i * k:(i+1)*k, :, :], (nv, d2 * d3 ) )

		#Calculate w histogram
		pdf_wap[i] = np.histogram( ndat[0], bins = bins * 100. / 60. / 60. / 24., density = True )[0]

		#Separate out into variables
		d = {'wap' : pd.Series(ndat[0]), 'tas' : pd.Series(ndat[1]), 'rlut' : pd.Series(ndat[2]), 'rsut' : pd.Series(ndat[3]), 'rsutcs' : pd.Series(ndat[4]), 'rlutcs' : pd.Series(ndat[5]),  'cf' : pd.Series(ndat[6]), 'swcf' : pd.Series(ndat[7]), 'lwcf' : pd.Series(ndat[8]) }
		df = pd.DataFrame(d)

		order = [ 6, 8, 2, 5, 3, 4, 7, 1, 0] #Since key order is different from order of data in input array

		#Now group everything by wap
		grouped = df.groupby(np.digitize(df.wap, bins = bins * 100. / 60. / 60. / 24.) )

		ms = np.zeros( ( nv, nb + 2 ) )
		means = np.zeros( ( nv, nb ) )

		lg = len(grouped.mean().wap[:])
		a = 0
		for key in grouped.mean():
			ms[order[a], :lg ] = grouped[key].mean()
			a += 1

		#Take means of bins
		a = 0
		for j in range( nb ):
			if ms[0, a] / 100. * 24. * 60. * 60. < min(bins): 
				#e.g if nothing in -100 to -90 bin, but have -107 datapoint
				means[:, j] = 0.
				a += 1
			if ms[0, a] / 100. * 24. * 60. * 60. < bins[j + 1]:
				means[:, j] = ms[:, a]
				a += 1	

		#Transfer data
		bin_dat[:, i, :] = means[:, :] #* pdf_wap[np.newaxis, :] to check that things sum up

	return bin_dat, pdf_wap
