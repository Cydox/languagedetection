import os

def getfreq(lst):
	""" Get frequency of characters in a list of strings """
	# initialize counters
	freqlist = [] # list of frequencies of characters a-z
	
	for x in range(26):
		freqlist.append(0.0)

	# count characters

	# loop though all characters
	for i in range(26):

		# loop through all strings
		for x in lst:

			# add the number of character chr(i + 97) (a-z) to the
			# respective element of freqlist (repeated for each string
			# in lst), ignoring the case of the letters.
			freqlist[i] += str.lower(x).count(chr(i + 97))
	
	# convert to frequency between 0 and 1
	numberOfCharacters = sum(freqlist)
	
	# divide each element in freqlist by total number of characters
	for i in range(len(freqlist)):
		freqlist[i] /= numberOfCharacters
	
	return freqlist
	
def getlang(folder):
	""" Get language ref info from txt file """

	lgnames = [] # list of language names
	lgfreqs = [] # list of frequency lists (for letters a-z)

	# Get filenames
	lst = os.listdir(folder) # list of filenames

	for fname in lst:
		
		#Get language name from file name, add to list
		lgnames.append(str.capitalize(fname.split(".")[0]))

		# Open file in folder to read
		f = open(folder + "/" + fname)

		# Read Reference texts and close file
		lines = f.readlines()
		f.close()

		# Get reference frequencies add to list of lists
		lgfreqs.append(getfreq(lines))

	return lgnames, lgfreqs

def getdiff(lst1, lst2):
	""" Get sum of the squared differences """
	
	# loop over each character while keeping a total of the squared differences
	# between lst1[i] and lst2[i]. This will return the square of the distance
	# between two 26 dimensional vectors.
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
