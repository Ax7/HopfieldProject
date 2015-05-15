import matplotlib.pyplot as plt
import hopfield_final
hn = hopfield_final.hopfield_network()

K = 10
P_size = 1
temp_error = 0
average_error = []
error = []
while(temp_error<=0.05):
	if (P_size % 5 == 0):
		print('Psize', P_size, ' av_error', temp_error)
	for i in range(1,K):
		error.append(hn.hopfield_run(P_size,100,0.8,1000,5,1,0.1))

	temp_error = sum(error)/K
	average_error.append(temp_error)
	P_size = P_size+1

plt.plot(range(1,P_size),average_error)
plt.savefig('Ex1_01.png')
