import inputdata
import numpy
import math
from scipy.stats.stats import pearsonr
data = inputdata.raw_scores

def norm2(x, y, A):
	return numpy.linalg.norm((A[x]-A[y])[numpy.logical_and( (A[x]) > 0, (A[y]) > 0)], 2)

def corr(x, y, A):
	return pearsonr(A[x][numpy.logical_and( (A[x]) > 0, (A[y]) > 0)], A[x][numpy.logical_and( (A[x]) > 0, (A[y]) > 0)])[0


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
	
main()


