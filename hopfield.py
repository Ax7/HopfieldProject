from copy import copy
import matplotlib as mpl
mpl.use('Agg')
from pylab import *

class hopfield_network:
	def __init__(self):
		''' lol '''

	def make_pattern(self,P=1,ratio=0.5):
		self.pattern = -ones((P,self.N**2),int)
		idx = int(ratio*self.N**2)
		for i in range(P):
			self.pattern[i,:idx] = 1
			self.pattern[i] = permutation(self.pattern[i])
		self.weight = zeros((self.N**2,self.N**2))
		for i in range(self.N**2):
			self.weight[i] = 1./self.N**2*sum(self.pattern[k,i]*self.pattern[k] for k in range(self.pattern.shape[0]))
		#print(self.pattern)

	def grid(self,mu=None):
		if mu is not None:
			x_grid = reshape(self.pattern[mu],(self.N,self.N))
		else:
			x_grid = reshape(self.x,(self.N,self.N))
		return x_grid

	def recall_step(self=0, lambda_w=1):
		# Update synaptic weights
		for i in range(self.N):
			for j in range(self.N):
				self.weight[i][j] = lambda_w*self.weight[i][j] + 1./self.N*self.x[i]*self.x[j]
		# Update network state
		h = sum(self.weight*self.x,axis=1)
		self.x = sign(h)

	def storage_step(self, mu=0, lambda_w=1):
		# Set network state to pattern mu
		self.x = copy(self.pattern[mu])

		# Update synaptic weights
		for i in range(self.N):
			for j in range(self.N):
				self.weight[i][j] = lambda_w*self.weight[i][j] + 1./self.N*self.x[i]*self.x[j]
		# Update network state
		h = sum(self.weight*self.x,axis=1)
		self.x = sign(h)

	def Hamming_distance(self,mu):
		return 0.5*(1-sum(self.pattern[mu]*self.x)/self.N**2)

	def run_phase(self,phase_type,c,mu,lambda_w,flip_ratio):
		if phase_type=='recall':
			self.x = copy(self.pattern[mu])
			flip = permutation(arange(self.N**2))
			idx = int(self.N**2*flip_ratio)
			self.x[flip[0:idx]] *= -1
			#print(self.x)
			for t in range(c):
				self.recall_step(lambda_w)
			self.error.append(self.Hamming_distance(mu))
			self.recall_phases+=1
			#print(self.weight)
			#print(self.x)
			#print(self.error)
		elif phase_type=='storage':
			for t in range(c):
				self.storage_step(mu,lambda_w)
			#print(self.weight)
			#print(self.x)

	def hopfield_run(self,pattern_dictionnary_size=1,patterns_size=10,p_storage=1,phases=1,time_steps=1,lambda_w=1,p_flip=0):
		self.N = patterns_size
		self.make_pattern(pattern_dictionnary_size,0.5)
		#print(self.pattern)
		self.recall_phases = 0
		self.error = []
		self.network_error = 0
		for i in range(phases):
			mu = int((pattern_dictionnary_size)*random())
			#print(mu)
			if(random()<p_storage):
				phase_type = 'storage'
				#print('Storage Phase')
			else:
				phase_type = 'recall'
				#print('Recall Phase')
			self.run_phase(phase_type,time_steps,mu,lambda_w,p_flip)
		if self.recall_phases>0:
			self.network_error = sum(self.error)/self.recall_phases
			#print(self.network_error)
		return self.network_error
