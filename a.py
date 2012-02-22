import inputdata
import numpy
data = inputdata.raw_scores

def main():
	persons = data.keys()
	papers = list()
	_papers = set();
	for i in data.values():
		for j in i.keys():
			_papers.add(j);
	for i in _papers:
		papers.append(i)
	A = numpy.ndarray((len(persons), len(papers)), dtype=float) 
	for i, j in data.iteritems():
		for k, l in j.iteritems():
			A[persons.index(i)][papers.index(k)] = l
	for i in range(len(persons)):
		for j in range(len(papers)):
			print str(persons[i]) + " " + str(papers[j]) + " " + str(A[i][j])

main()


