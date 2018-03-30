#!/usr/bin/env python
import random
import sys
import time

def in_circle(x, y):
	if (x*x+y*y) <= 1:
		return True
	else:
		return False

def count_hits(number_of_points):
    number_of_hits = 0

    for counter in range (0, number_of_points):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if in_circle(x,y):
            number_of_hits += 1

    return number_of_hits

def count_pi(points_in_total):
	start_time = time.time()
	hits = count_hits(points_in_total)
	pi = 4*float(hits)/float(points_in_total)
	total_time = time.time() - start_time
	print(str(pi))
	print(total_time)

def main():
    points_in_total = int(sys.argv[1])
    count_pi(points_in_total)

if __name__ == "__main__":
    main()
