"""

	Tom Wallis
	GUTS Hackathon 2014

	Python script to convert CSV file into Python nested list.
	This is used as a poor man's alternative to MySQL, as we don't have to actually deploy.

"""

# THIS NEEDS FIXING SO WE CAN CONVERT THE DATA FROM DICTIONARIES AND REDUCE THE SIZE OF THE INPUT. 
# import Dicts



def csvToList(filepath = './terrordb.csv'):
	
	result = []
	
	# Open the file as TerrorCSV, and add each row to the results as an array. 
	with open(filepath, 'r') as terrorCSV:
		for row in terrorCSV:

			# The magic line! Take the row from terrorCSV, remove whitespace, and make a list out of it, splitting at the commas. 
			# ...then, add the list to the results. 
			result.append( [ row.rstrip().split(',') ] )


	return result



class TerrorDB(object):
	"""A class that allows for easy access to data from the Terror DB"""
	
	"""self.terrorRecord is a nested list, so that we can index into whatever type of information we want. Methods below will simplify this."""

	def __init__(self, filepath = './terrordb.csv'):
		super(TerrorDB, self).__init__()
		self.terrorRecord = csvToList(filepath)


	def getCategories(self):
		return self.terrorRecord[0]

	def dumpAll(self):
		return self.terrorRecord

	def getIDs(self):
		return self.terrorRecord[1]

	def convertRegions(self):
		regionLocation = self.getCategories.index('region')

