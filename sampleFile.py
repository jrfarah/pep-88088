"""
====================================
Filename:		sampleFile.py 
Author:			Joseph Farah 
Description:	An example file to demonstrate the PEP-88088 style proposal. 
                Will display some sample matplotlib plots. 
====================================
Notes
	 Notes and TODOs go here. 
"""

## imports ##
import random
import itertools
import matplotlib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

## global settings ##

## matplotlib settings ##
plt.rcParams['grid.color'] 			= 'k'												## color of the grid lines
plt.rcParams['grid.linestyle'] 		= ':'												## style of the grid lines
plt.rcParams['grid.linewidth'] 		= 0.8												## grid linewidth 
plt.rcParams["font.family"] 		= "Times New Roman"									## font
plt.rcParams['xtick.direction'] 	= 'in'												## x tick direction
plt.rcParams['ytick.direction'] 	= 'in'												## y tick direction
plt.rcParams['axes.linewidth'] 		= 2 												## global linewidth
colors 								= [													## colormaps
										"windows blue", 	
										"amber", 
										"greyish", 
										"faded green", 
										"dusty purple"
									]
cycol 								= itertools.cycle(sns.color_palette("bone", 8))		## color cycle definition
plt.rcParams.update({'font.size': 16})													## font size update
matplotlib.rcParams.update({'errorbar.capsize': 2})										## errorbar capsize
plt.rcParams.update({'mathtext.default':  'regular' })									## math enabling


## global variables ##
DATASET_RESOLUTION 	= 50		## resolution of the fake datasets generated
TIME_START			= 0			## start time
TIME_END			= 1			## end time 


class Data(object):
 	"""
 		Contains x and y data for a dataset.

 	"""
 	def __init__(self, x, y):
 		"""
 		    Initializes the class.
 		
 		    Args:
 		        x (list): List of x values in a dataset. 
 		        y (list): List of y values in a dataset. 
 		
 		    Returns:
 		        none (none): none
 		
 		"""
 		
 		## add input arguments as attributes ##
 		self.x = x 
 		self.y = y


 	def squareY(self):
 		"""		
 		    Square the y portion of the dataset. 
 		    Operates on self.y in place. 
 		
 		    Args:
 		        none (none): none
 		
 		    Returns:
 		        none (none): none
 		
 		"""
 		
 		## square the y portion element-wise ##
 		self.y = [yElement**2 for yElement in self.y]


def main():
	"""
	    Main function flow.
	
	    Args:
	        none (none): none
	
	    Returns:
	        none (none): none
	
	"""
	
	## define an x dataset ##
	xDataset = np.linspace(TIME_START, TIME_END, DATASET_RESOLUTION)

	## define first subplot, linear relationship with noise and error ##
	plt.subplot(221)
	plt.xlim(TIME_START, TIME_END)

	## define initial non-noisy set ##
	linY = xDataset

	## add noise to linY ##
	linY = [y + 0.2*(random.random() - 0.5) for y in linY]

	## generate fake error bars ##
	errLinY = [0.2*random.random() for y in linY]
	plt.errorbar(xDataset, linY, yerr=errLinY, fmt='d', color='orange', label='data')

	## create fit line ##
	fitLine = xDataset

	## plot fit line ##
	plt.plot(xDataset, fitLine, linestyle='--', color='black', zorder=999, label='best fit')

	## set labels ##
	plt.xlabel("Intensity ($\phi$)")
	plt.ylabel("Temperature ($\Omega$)")

	## figure post processing ##
	plt.tick_params(length=5)
	plt.legend()
	plt.minorticks_on()
	plt.tick_params('both', which='minor', length=6)
	plt.grid()


	## define second subplot, quadratic relationship with noise and error ##
	plt.subplot(222)
	plt.xlim(TIME_START, TIME_END)

	## define initial non-noisy set ##
	linY = xDataset

	## create data object and square the Y values ##
	dataObject = Data(xDataset, linY)
	dataObject.squareY()

	## add noise to linY ##
	dataObject.y = [y + 0.05*(random.random() - 0.5) for y in dataObject.y]

	## generate fake error bars ##
	errLinY = [0.2*random.random() for y in dataObject.y]
	plt.errorbar(xDataset, dataObject.y, yerr=errLinY, fmt='d', color="green", label='best fit')

	## create fit line ##
	fitLine = xDataset

	## plot fit line ##
	plt.plot(xDataset, fitLine**2, linestyle='--', color='black', zorder=999, label='fit line')

	## set labels ##
	plt.xlabel("Intensity ($\phi$)")
	plt.ylabel("Temperature ($\Omega$)")

	## figure post processing ##
	plt.tick_params(length=5)
	plt.legend()
	plt.minorticks_on()
	plt.tick_params('both', which='minor', length=6)
	plt.grid()


	## third subplot, random histogram ##
	plt.subplot(223)

	## make the data ##
	data = [random.gauss(1, 0.5) for i in range(DATASET_RESOLUTION*1000)]

	## make histogram ##
	plt.hist(data, bins=75, edgecolor='black', color='lightblue')

	## set labels ##
	plt.xlabel("Chi-square ($\mu=1$)")
	plt.ylabel("Entries ($\eta$)")

	## figure post processing ##
	plt.tick_params(length=5)
	plt.legend()
	plt.minorticks_on()
	plt.tick_params('both', which='minor', length=6)
	plt.grid()

	## fourth subplot,  ##
	plt.subplot(224)

	## make the data ##
	data = [random.gauss(1.0, 0.5) for i in range(DATASET_RESOLUTION*1000)]
	data2 = [random.gauss(1.5, 0.3) for i in range(DATASET_RESOLUTION*1000)]

	## make histogram ##
	plt.hist(data, bins=75, edgecolor='black', color='lightblue', alpha=0.7)
	plt.hist(data2, bins=75, edgecolor='black', color='orange', alpha=0.7)

	## set labels ##
	plt.xlabel("Chi-square ($\mu=1$)")
	plt.ylabel("Entries ($\eta$)")

	## figure post processing ##
	plt.tick_params(length=5)
	plt.legend()
	plt.minorticks_on()
	plt.tick_params('both', which='minor', length=6)
	plt.grid()





	## show entire plot ##
	plt.show()
	

if __name__ == '__main__':
	main()