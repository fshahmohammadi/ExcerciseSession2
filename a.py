import inputdata
import numpy
import math
from scipy.stats.stats import pearsonr
data = inputdata.raw_scores

def norm2(x, y, A):
	return numpy.linalg.norm((A[x]-A[y])[numpy.logical_and( (A[x]) > 0, (A[y]) > 0)], 2)

def corr(x, y, A): 
	return pearsonr(A[x][numpy.logical_and( (A[x]) > 0, (A[y]) > 0)], A[y][numpy.logical_and( (A[x]) > 0, (A[y]) > 0)])[0]

def SimilarResearcher(x, A, persons):
	return [(sorted([(norm2(x, i, A), persons[i])  for i in range(len(A[x]))])[1:6]) [j][1] for j in range(5)]  

def SimilarPapers(x, A, papers): 
	return [(sorted([(norm2(x, i, numpy.transpose(A)), papers[i])  for i in range(len(A[x]))])[1:6]) [j][1] for j in range(5)]  

#def RecommendPaper(x, A, persons):
		


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
	Num2 = [([norm2(i, j, A) for j in range(len(persons))]) for i in range(len(persons))]
	Corr = [([corr(i, j, A)  for j in range(len(persons))]) for i in range(len(persons))]
	print SimilarPapers(0, A, papers)
	
'''	
	print "--------------------persons--------------"
	print persons
	print "--------------------papers---------------"
	print papers
	print "--------------------likes----------------"
	print A
	print "--------------------norm2 distanses------"
	print Num2
	print "--------------------corrilations---------"
	print Corr
	print SimilarResearcher(0, A, persons)
'''
	
main()


