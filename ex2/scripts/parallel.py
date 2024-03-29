#!/usr/bin/env python
from mpi4py import MPI
import random
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def print_result(pi, time, processors, points):
	print(str(pi)+','+str(time)+','+str(processors)+','+str(points))

def count_hits(number_of_points):
	number_of_hits = 0

	for counter in xrange(0, number_of_points):
		x = random.uniform(0,1)
		y = random.uniform(0,1)
		if (x*x+y*y) <= 1:	#  in circle
			number_of_hits += 1

	return number_of_hits

def count_pi(type, points):
	if type == 'scalable':
		points_in_total = points * size
	else:
		points_in_total = points

	comm.barrier()
	if rank == 0:
		start = MPI.Wtime()

	hits = count_hits(points_in_total/size)
	all_hits = comm.gather(hits, root=0)

	if rank == 0:
		end = MPI.Wtime()
		all_hits_count = 0
		for h in all_hits:
			all_hits_count += h
		pi = 4*float(all_hits_count)/float(points_in_total)
		time = end - start
		print_result(pi, time, size, points)

def main():
	type = sys.argv[1]
	points = int(sys.argv[2])

	if type == 'scalable' or type == 'nonscalable':
		count_pi(type, points)
	else:
		print('Please specify scalable or nonscalable parallelization')
		exit()

if __name__ == "__main__":
	main()
