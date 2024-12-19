# 16-12-2024
# https://www.deep-ml.com/problem/Confusion%20Matrix%20for%20Binary%20Classification

from collections import Counter

def confusion_matrix(data):
	tuple_data=[]
	
	for pair in data:
	    tuple_data.append(tuple(pair))
	    
	counts = Counter(tuple_data)
	
	TP, FN, FP, TN = counts[(1, 1)], counts[(1, 0)], counts[(0, 1)],counts[(0, 0)]
	
	confusion_matrix = [[TP,FN], [FP, TN]]

	print(confusion_matrix)
	return confusion_matrix
	pass
