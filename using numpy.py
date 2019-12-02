
import numpy
N=input() 
a = numpy.array([int(i) for i in input().strip().split(' ')])
print(numpy.percentile(a, range(0, 100, 25), interpolation = 'midpoint'))
print(numpy.percentile(a, 50))

