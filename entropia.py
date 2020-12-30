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

	def zero(self):
		"""This method determine the real zero precision"""

		float_epsilon = np.finfo(float).eps
		print(float_epsilon)
		float32_eps = np.finfo(np.float32).eps
		print(float32_eps)

w = entropia()
#w.zero()

def entropy1(labels, base=None):
	""" Define entropy function 1"""
	value,counts = np.unique(labels, return_counts=True)
	return entropy(counts, base=base)

def entropy2(labels, base=None):
	""" Computes entropy of label distribution. """

	n_labels = len(labels)

	if n_labels <= 1:
		return 0

	value,counts = np.unique(labels, return_counts=True)
	probs = counts / n_labels
	n_classes = np.count_nonzero(probs)

	if n_classes <= 1:
		return 0

	ent = 0.

	# Compute entropy
	base = e if base is None else base
	for i in probs:
		ent -= i * log(i, base)

	return ent

def entropy3(labels, base=None):
	vc = pd.Series(labels).value_counts(normalize=True, sort=False)
	base = e if base is None else base
	return -(vc * np.log(vc)/np.log(base)).sum()

def entropy4(labels, base=None):
	value,counts = np.unique(labels, return_counts=True)
	norm_counts = counts / counts.sum()
	base = e if base is None else base
	return -(norm_counts * np.log(norm_counts)/np.log(base)).sum()

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
				print(f'Jogo igual na linha {p}')

	except:
		continue

print(j)
print(entropy1(j))
