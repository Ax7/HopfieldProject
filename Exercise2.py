import hopfield
import matplotlib.pyplot as plt

hn = hopfield.hopfield_network()

N_vec = []
dictionarySize_vec = []

nbOfTests = 2
targetError = 0.05
sigmaError = 0.001
networkSizeMin = 10
networkSizeMax = 20
networkStep = 2
networkSizeList = xrange(networkSizeMin, networkSizeMax + 1, networkStep)

def computeBoundError(bound, networkSize, nbOfTests, hn):
	recordedError = []
	for i in xrange(1, nbOfTests):
		recordedError.append(hn.hopfield_run(bound, networkSize, 0.8, 1000, 5, 1, 0.1))
	return sum(recordedError)/nbOfTests

for netSize in networkSizeList:
	print '['+str(netSize)+']', ' --- starting ---'
	lowerBound = 1
	upperBound = 100
	lowerBoundError = 0
	# Compute upperBound error
	upperBoundError = computeBoundError(upperBound, netSize, nbOfTests, hn)
	while(abs(lowerBoundError - targetError) > sigmaError and abs(upperBound - lowerBound) > 1 and lowerBoundError < targetError):
		# Bigger then upperBound
		if(upperBoundError < targetError):
			# We set the lowerBound to upperBound and double the distance of upperBound form lowerBound
			tmp = upperBound
			upperBound += abs(upperBound - lowerBound)
			lowerBound = tmp
			lowerBoundError = upperBoundError
			upperBoundError = computeBoundError(upperBound, netSize, nbOfTests, hn)
		# Smaller then upperBound
		else:
			# We reduce by 2 the distace of upperBound to lowerBound
			upperBound -= int( abs(upperBound - lowerBound) / 2 )
			upperBoundError = computeBoundError(upperBound, netSize, nbOfTests, hn)
		print '['+str(netSize)+']', 'lower:', lowerBound, '('+str(lowerBoundError)+')', 'upper:', upperBound, '('+str(upperBoundError)+')'
	print '['+str(netSize)+']', ' --- result:', lowerBound, '('+str(lowerBoundError)+') ---'
	dictionarySize_vec.append(lowerBound)
	N_vec.append(netSize)

# Generating the plot
plt.plot(N_vec,dictionarySize_vec, 'bo-')
plt.xlabel('Network size')
plt.ylabel('Dictionary size')
plt.title('Exercice 2 - Threshold ' + str(targetError) + r'$- \sigma$ (' + str(sigmaError) + ')')
plt.grid(True)
plt.savefig('Ex2_01.png')

