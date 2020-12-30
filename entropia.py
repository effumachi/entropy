"""F_bot Program."""
__author__ = "Fumachi"
__copyright__ = "Copyright 2020, Fumachi"
__credits__ = "PyClass.com.br"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Fumachi"
__email__ = "effumachi@gmail.com"
__status__ = "Production"
import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd
import timeit

class entropia():

	def __init__(self):
		"""Somente inicializacao"""
		pass

	def calculoTeste(self):
		"""Executa um calculo"""
		calculo = 1



if __name__ == '__main__':
	entropia()


#w.zero()

def entropy1(labels, base=None):
	""" Define entropy function 1"""
	value,counts = np.unique(labels, return_counts=True)
	return entropy(counts, base=base)


#labels = [1,3,5,2,3,5,3,2,1,3,4,5]
#labels1 = [1,3,5,2,3,5,3,2,1,3,4,5,5,5,2]
vec = [[25, 7, 20, 14, 6, 12, 17, 24, 16, 19, 23, 21, 9, 13, 2]]
v1 = [[1,2,3], [2,3,4]]
from random import randint
n = []
i = 0
while len(n) < 4:
	i += 1
	n.append(i)
print(n)
w = n


j = []
while len(j) < 3:
	try:
		x = w[randint(0, len(w))]
		j.append(x)
		n.remove(x)
		w = n
	except :
		continue

	try:
		for p in v1:
			if j == p:
				print(f'line {p}')

	except:
		continue

print(j)
print(entropy1(j))
