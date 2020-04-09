#Run "pip3 install opencv-python" in CLI
import sys, os
import matplotlib.pyplot as plt
import csv

# Store command line arguments in variables
filename = sys.argv[1]
title = sys.argv[2]
varX = sys.argv[3]
varY = sys.argv[4]

# Open the data file
data = open(filename, 'r')
data = csv.reader(data)

x = []
y = []

for obs in data:
    x.append(obs[0])
    y.append(obs[1])

# Plot the data
plt.plot(x,y, 'o')
plt.xlabel(varX)
plt.ylabel(varY)
plt.title(title)
plt.savefig("graph.pdf")
if sys.platform == "win32":
    os.system("explorer.exe graph.pdf")
else:
    os.system("open graph.pdf")
#print("File created: graph.pdf at location {}".format(os.getcwd()))
