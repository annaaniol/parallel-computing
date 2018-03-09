#!/usr/bin/env python
from mpi4py import MPI
import random
import csv
import sys
import socket

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
msgSize = int(sys.argv[1])
counter = 0

print("my rank is: %d, at node %s"%(comm.rank, socket.gethostname()))

def randomBytes(n):
    return bytearray(random.getrandbits(8) for i in range(n))

data = randomBytes(msgSize)
start = MPI.Wtime();

while MPI.Wtime() < start + 1:
	
	if rank == 0:
		req = comm.isend(data, dest=1)
		req.wait()
	elif rank == 1:
   		req = comm.irecv(None, dest=0)
		data = req.wait()
		counter += 1		
   	else:
   		print "Expected only two nodes"
# bit/s
capacity = counter * msgSize/8
# Mbit/s
capacity /= float(1000000)

if rank==1:	
	with open('capacityResults.csv', 'a') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(['nonblocking',msgSize,str(counter)])
	print ("executed: %d times"%(counter))
	print ("capacity: %f Mbit/s"%(capacity))
