import inputdata
import numpy
import math
from scipy.stats.stats import pearsonr
data = inputdata.raw_scores

def norm2(x, y, A):
	return numpy.linalg.norm((A[x]-A[y])[numpy.logical_and( (A[x]) > 0, (A[y]) > 0)], 2)

def corr(x, y, A):
	return pearsonr(A[x][numpy.logical_and( (A[x]) > 0, (A[y]) > 0)], A[y][numpy.logical_and( (A[x]) > 0, (A[y]) > 0)])[0]


def main():
	persons = data.keys()
	papers = list()
	_papers = set();
	for i in data.values():
		for j in i.keys():
			_papers.add(j);
	for i in _papers:
		papers.append(i)
	A = numpy.zeros((len(persons), len(papers)), dtype=float) 
	
	for i, j in data.iteritems():
		for k, l in j.iteritems():
			A[persons.index(i)][papers.index(k)] = l
	
	Num2 = numpy.zeros((len(persons), len(persons)), dtype=float) 
	Corr = numpy.zeros((len(persons), len(persons)), dtype=float) 
	for i in range(len(persons)): 
		for j in range(len(persons)):
			Num2[i][j] = norm2(i, j, A)
			Corr[i][j] = corr(i, j, A) 
	
	print "--------------------persons--------------"
	print persons
	print "--------------------papers---------------"
	print papers
	print "--------------------likes----------------"
	print A
	print "--------------------norm2----------------"
	print Num2
	print "--------------------Curr-----------------"
	print Corr

	
main()


