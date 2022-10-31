# #############################################################################
# given a set of spacetime events sprinkled from a poisson distribution, 
# the purpose of this algorithm is to determine which events are
# causally related
# use this set of ordered_pairs to reconstruct image in paper
# ordered_pairs = [
# (0.998021388064573, 0.2944865268154061), 
# (0.43824718181429445, 0.3112214246861015), 
# (0.25544571062019517, 0.27362195983385273), 
# (0.28194840623114203, 0.42007977225100346), 
# (0.001644987048430302, 0.31238826775251605), 
# (0.13522268275888483, 0.5452917088831439), 
# (0.22766058753436313, 0.5063588556538683), 
# (0.9110184724379343, 0.003733951950835701), 
# (0.14507589913444652, 0.10412415225304184), 
# (0.9697655084758309, 0.675222065832517), 
# (0.8023595301779428, 0.8998233750930827), 
# (0.2015062018978766, 0.9509422555380234), 
# (0.5440584201394114, 0.1080192595916678), 
# (0.2633575476901, 0.4249575857238266)]
# #############################################################################

import numpy as np
from matplotlib import pyplot as plt 
from scipy.stats import poisson
import networkx as nx


# generate points
def generate_events(mean=10):
	"""
	"""
	# generate a number of events from a poisson distribution with given mean
	num_points = np.random.poisson(mean)
	
	u = np.random.rand(num_points)
	v = np.random.rand(num_points)
	ordered_pairs = list(zip(u, v))
	return u, v, ordered_pairs

def generate_excision(length = 0.5 * np.sqrt(2)):
	"""
	"""
	delta_u = length / np.sqrt(2)
	u1 = 0.5 - (0.5 * delta_u)
	u2 = 0.5 + (0.5 * delta_u)
	v1 = -u1 + 1
	v2 = -u2 + 1
	return u1, u2, v1, v2

def generate_edges(graph, u1, u2, v1, v2, ordered_pairs):
	"""
	"""
	for u, v in ordered_pairs:
		if (u1 < u < u2) and (v2 < v < -u + 1):  # region I
			for u_prime, v_prime in ordered_pairs:
				if (u_prime > u) and (v_prime > v) and (u1 < u_prime < u2) and (v2 < v_prime < -u_prime + 1):
					graph.add_edge((u, v), (u_prime, v_prime))
		elif ((0 < u < u1) and (0 < v < v2)):  # region II
			for u_prime, v_prime in ordered_pairs:
				if (u_prime > u) and (v_prime > v) and not((u1 < u_prime < u2) and (-u_prime + 1 < v_prime < v1)):
					graph.add_edge((u, v), (u_prime, v_prime))
		elif (0 < u < u1) and (v2 < v < v1):  # region III
			for u_prime, v_prime in ordered_pairs:
				if (u_prime > u) and (v_prime > v) and not((u1 < u_prime < 1) and -u_prime + 1 < v_prime < v1):
					graph.add_edge((u, v), (u_prime, v_prime))
		elif (u1 < u < u2) and (0 < v < v2):  # region III'
			for u_prime, v_prime in ordered_pairs:
				if (u_prime > u) and (v_prime > v) and not((u1 < u_prime < u2) and (-u_prime + 1 < v_prime < 1)):
					graph.add_edge((u, v), (u_prime, v_prime))
		else:  # 
			for u_prime, v_prime in ordered_pairs:
				if (u_prime > u) and (v_prime > v):
					graph.add_edge((u, v), (u_prime, v_prime))

def generate_():
	...


if __name__ == '__main__':
	u, v, ordered_pairs = generate_events()

	u1, u2, v1, v2 = generate_excision()
	plt.plot((u1, u2), (v1, v2), color = 'red')

	G = nx.DiGraph()
	G.add_nodes_from(ordered_pairs)

	generate_edges(G, u1, u2, v1, v2, ordered_pairs)

	H = nx.transitive_reduction(G)
	nx.draw(G)
	plt.draw()

	for red_n in H:
		for red_m in H:
			if H.has_edge(red_n, red_m):
				red_m_u = red_m[0]
				red_m_v = red_m[1]
				red_n_u = red_n[0]
				red_n_v = red_n[1]
				# plt.plot([red_m_u, red_n_u], [red_m_v, red_n_v], color = 'green')


	plt.scatter(u, v)
	plt.axis('square')
	plt.xlim(0,1)
	plt.ylim(0,1)
	# plt.show()
