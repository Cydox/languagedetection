import os

def getfreq(lst):
	""" Get frequency of characters in a list of strings """
	# initialize counters
	freqlist = []
	for x in range(26):
		freqlist.append(0.0)

	# count characters

	for i in range(26):
		for x in lst:
			freqlist[i] += str.lower(x).count(chr(i + 97))
	
	# convert to frequency

	numberOfCharacters = sum(freqlist)

	for i in range(len(freqlist)):
		freqlist[i] /= numberOfCharacters
	
	return freqlist
	
def getlang(folder):
	""" Get language ref info from txt file """

	lgnames = []
	lgfreqs = []

	# Get filenames

	lst = os.listdir(folder)

	for fname in lst:
		
		#Get language name from file name, add to list
		
		lgnames.append(str.capitalize(fname.split(".")[0]))

		# Open file in folder to read
		
		f = open(folder + "/" + fname)

		# Read Reference texts

		lines = f.readlines()
		f.close()

		# Get reference frequencies add to list of lists
		
		lgfreqs.append(getfreq(lines))

	return lgnames, lgfreqs

def getdiff(lst1, lst2):
	""" Get sum of the squared differences """

	total = 0
	for i in range(26):
		total += (lst1[i] - lst2[i]) * (lst1[i] - lst2[i])
	
	return total

def getIndexOfMinVal(lst):
	""" Find index of smallest value in a list """
	
	#initialize current min value and index to first element

	minIndex = 0 # index of current minimal value
	val = lst[0] # current minimal value

	# loop through all elements

	for i in range(1, len(lst)):
		
		# if current value is smaller than current minimum -> update values

		if lst[i] < val:
			minIndex = i
			val = lst[i]
	return minIndex
