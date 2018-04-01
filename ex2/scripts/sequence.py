#!/usr/bin/env python
import random
import sys
import time

def count_hits(number_of_points):
	number_of_hits = 0

	for counter in xrange(0, number_of_points):
		x = random.uniform(0,1)
		y = random.uniform(0,1)
		if (x*x+y*y) <= 1:	#  in circle
			number_of_hits += 1

	return number_of_hits

def count_pi(points_in_total):
	start_time = time.time()
	hits = count_hits(points_in_total)
	pi = 4*float(hits)/float(points_in_total)
	total_time = time.time() - start_time
	return total_time

def main():
	points_in_total = int(sys.argv[1])
	times = []
	for i in range (0, 10):
		times.append(count_pi(points_in_total))
	print(str(points_in_total) + ',' + str(min(times)))

if __name__ == "__main__":
	main()
