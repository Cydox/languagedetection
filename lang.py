from langtools import *
import matplotlib.pyplot as plt

fname = str(raw_input("File name: "))

f = open(fname, "r")
lines = f.readlines()
f.close()

freq = getfreq(lines)
lgnames, lgfreq = getlang("data")

diffs = [0.0, 0.0, 0.0, 0.0]

for i in range(len(lgnames)):
        diffs[i] = (getdiff(freq, lgfreq[i]))

i = getIndexOfMinVal(diffs)
print "Language:", lgnames[i]

plt.suptitle("Language fingerprints")
xbar = range(26)

plt.subplot(321)
plt.title(fname)
plt.bar(xbar, freq, 0.6, color="r")

for i in range(4):
	plt.subplot(323 + i)
	plt.title(lgnames[i])
	plt.bar(xbar, lgfreq[i], 0.6, color="b")
	plt.plot(freq, "r.")



plt.show()
