#!/usr/bin/env python
from mpi4py import MPI
import random
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

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
	comm.barrier()
	start = MPI.Wtime()

	hits = count_hits(points_in_total/size)
	all_hits = comm.gather(hits, root=0)

	if rank == 0:
		end = MPI.Wtime()
        all_hits_count = 0
	    for h in all_hits:
            all_hits_count += h
		pi = 4*float(all_hits_count)/float(size*points_in_total)
		print(str(pi))

		time = end - start
		print(str(time))


def main():
    points_in_total = int(sys.argv[1])
    count_pi(points_in_total)

if __name__ == "__main__":
    main()
