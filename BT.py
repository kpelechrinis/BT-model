from matplotlib import pyplot as plt
import sys
import seaborn as sns
import pandas as pd
import numpy as np
from scipy import optimize
import choix

df = pd.read_csv("nba1617.csv")
teams = list(set(df.Home.unique()))
t = list(np.sort(teams))

data = []

for i in range(len(df.Visitor)):
	if df.PTSV[i] > df.PTSH[i]:
		el = (t.index(df.Visitor[i]),t.index(df.Home[i]))
	else:
		el = (t.index(df.Home[i]),t.index(df.Visitor[i]))
	data.append(el)

skills = choix.ilsr_pairwise(30, data)



for i in range(30):
	win_probs = []
	for j in range(30):
		win_probs.append(choix.probabilities([i, j], skills)[0])
	print win_probs
		
