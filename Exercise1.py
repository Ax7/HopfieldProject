import hopfield
import matplotlib.pyplot as plt

# Parameters:
# Number of error to be averaged
nbOfTests = 10
# The size of the network
networkSize = 100
# Our targeted threshold error
targetError = 0.05

# Variable
hn = hopfield.hopfield_network()
dictionarySize = 1
averagedError = [0]
recordedError = []

print '--- Start ---'
while(averagedError[-1] <= targetError):
	# Prints every 5 iterations
	if (dictionarySize % 5 == 0):
		print('Dictionary size', dictionarySize, 'tmpError', averagedError[-1])
	# Loop for averaging the errors
	for i in xrange(1,nbOfTests):
		recordedError.append(hn.hopfield_run(dictionarySize, networkSize, 0.8, 1000, 5, 1, 0.1))
	# Average the errors and stors it
	averagedError.append(sum(recordedError)/nbOfTests)
	# Increas dictionary size
	dictionarySize += 1

# Generating the plot
print '--- Generating plots ---'
plt.plot(xrange(1,dictionarySize), averagedError[1:], 'bo-', [1, dictionarySize], [targetError, targetError], 'r--')
plt.xlabel('Dictionary size')
plt.ylabel('Averaged error')
plt.title('Exercice 1 - Nework size ' + str(networkSize))
plt.grid(True)
plt.savefig('Ex1_01.png')
print '--- Finished ---'
