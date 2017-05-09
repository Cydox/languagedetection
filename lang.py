from langtools import *
import matplotlib.pyplot as plt

# get filename of file to be evaluated from user
# use raw_input, because we want a string
fname = str(raw_input("File name: "))

# open, read and close file
f = open(fname, "r")
lines = f.readlines() # list of lines (strings)
f.close()

# calculate frequency of each letter in the file
freq = getfreq(lines)

# get frequency of each letter from reference files
lgnames, lgfreq = getlang("data")

#calculate difference between frequencies of file and each refence files
diffs = []

for i in range(len(lgnames)):
        diffs.append(getdiff(freq, lgfreq[i]))

# find the language with the lowest difference and print it
i = getIndexOfMinVal(diffs)
print "Language:", lgnames[i]

# draw graph for tested file
plt.suptitle("Language fingerprints")
xbar = range(26)

plt.subplot(321)
plt.title(fname)
plt.bar(xbar, freq, 0.6, color="r")

# draw graph for reference files
for i in range(4):
	plt.subplot(323 + i)
	plt.title(lgnames[i])
	plt.bar(xbar, lgfreq[i], 0.6, color="b")
	plt.plot(freq, "r.")

plt.show()
