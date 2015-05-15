import hopfield_final

hn = hopfield_final.hopfield_network()

for i in range(1, 100):
	print hn.hopfield_run(i, 10, 0.8, 1000, 5, 1, 0.1)
