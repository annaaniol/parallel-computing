#!/usr/bin/env python
from mpi4py import MPI
import random
import csv
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
msgSize = int(sys.argv[1])
sumDelay = 0

def randomBytes(n):
    return bytearray(random.getrandbits(8) for i in range(n))

for i in range (0,100):
	
	data = randomBytes(msgSize)
	start = MPI.Wtime();
	
	if rank == 0:
		comm.send(data, dest=1)
	elif rank == 1:
   		data = comm.recv(source=0)
		end = MPI.Wtime() - start
		sumDelay += end   		
	else:
   		print "Expected only two nodes"

avgDelay = sumDelay*10

if rank==1:	
	with open('delayResults.csv', 'a') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['blocking',msgSize,str(avgDelay)])
	print ("blocking comunication delay: %f ms"%avgDelay)
