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

# Initialize variables
x = []
y = []
null = 0

# Add data to variables
for obs in data:
    try:
        # make sure both variables are ints/floats
        float(obs[0])
        float(obs[1])
        # if so, add them to the lists
        x.append(float(obs[0]))
        y.append(float(obs[1]))
    except:
        # otherwise add a null value without appending anything to the lists
        null += 1

# Plot the data
plt.plot(x,y, 'o')
plt.xlabel(varX)
plt.ylabel(varY)
plt.title(title)

# Save and open figure
plt.savefig("graph.pdf")
if sys.platform == "win32":
    os.system("explorer.exe graph.pdf")
else:
    os.system("open graph.pdf")

# Display some helpful output
print("File created: graph.pdf at location {}".format(os.getcwd()))
print("There were " + str(null) + " null, titles, or incorrectly formatted values in the dataset.")
