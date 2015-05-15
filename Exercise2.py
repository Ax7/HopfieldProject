import matplotlib.pyplot as plt
import hopfield_final
hn = hopfield_final.hopfield_network()

npoints = 5
K = 10
N_vec = []
P_size_vec = []
temp_error = 0
lowerbound = 1
upperbound = 100
P_size = 50
error = []
l_error = 0
u_error = 0
target_error = 0.05
temp_error = 10
for N in xrange(100,1000,(1000-100)/npoints):

    while(abs(temp_error-target_error)>0.005):
    	#if (P_size % 5 == 0):
    	#	print('Psize', P_size, ' av_error', temp_error)

        error = []
    	for i in range(1,K):
    		error.append(hn.hopfield_run(P_size,N,0.8,1000,5,1,0.1))
        temp_error = sum(error)/K

        if(temp_error>target_error):
            upperbound = P_size
            u_error = temp_error

            error = []
            for i in range(1,K):
    	   	   error.append(hn.hopfield_run(lowerbound,N,0.8,1000,5,1,0.1))
            l_error = sum(error)/K

        else:
            lowerbound = P_size
            l_error = temp_error
            error = []
            for i in range(1,K):
    		  error.append(hn.hopfield_run(upperbound,N,0.8,1000,5,1,0.1))
            u_error = sum(error)/K

        if (target_error>u_error):
            lowerbound = upperbound
            upperbound = upperbound*2

        print('lerror',l_error)
        print('uerror',u_error)
        temp_error = (upperbound + lowerbound) / 2
        P_size = int((upperbound+lowerbound)/2)
        print('lbound',lowerbound)
        print('ubound',upperbound)

    P_size_vec.append(P_size)
    N_vec.append(N)

plt.plot(N_vec,P_size_vec)
plt.savefig('Ex2_01.png')
