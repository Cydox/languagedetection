import os

def getfreq(lst):
	""" Get frequency of characters in a list of strings """
	# initialize counters
	numberOfCharacters = 0
	freqlist = []
	for x in range(26):
		freqlist.append(0.0)
	
	# count characters
	for x in lst:
		for y in x:
			a = ord(str.lower(y)) - 97
			if a >= 0 and a <= 25:
				freqlist[a] += 1
				numberOfCharacters += 1
	
	# convert to frequency

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
	minIndex = 0
	val = lst[0]

	for i in range(len(lst)):
		if lst[i] < val:
			minIndex = i
			val = lst[i]
	return minIndex
