#!/usr/bin/env python
from mpi4py import MPI
import random
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def print_result(pi, time, type, size, points):
	print(str(pi)+','+str(time)+','+type+','+str(size)+','+str(points))

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
	comm.barrier()

	if rank == 0:
		end = MPI.Wtime()
		all_hits_count = 0
		for h in all_hits:
			all_hits_count += h
		pi = 4*float(all_hits_count)/float(points_in_total)
		time = end - start
		if type == 'scalable':
			print_result(pi, time, 'scalable', size, points)
		else:
			print_result(pi, time, 'nonscalable', size, points_in_total)


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
