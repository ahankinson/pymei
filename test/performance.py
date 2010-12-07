import cProfile
import itertools

cProfile.run('itertools.ifilter(lambda x: x % 2 == 0, xrange(10000))')

print("------")

cProfile.run('filter(lambda x: x % 2 == 0, xrange(10000))')
