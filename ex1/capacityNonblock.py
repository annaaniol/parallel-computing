#!/usr/bin/env python
from mpi4py import MPI
import random
import csv
import sys
import socket

def randomBytes(n):
    return bytearray(random.getrandbits(8) for i in range(n))

def measureCapacity(msgSize):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    # print("my rank is: %d, at node %s"%(comm.rank, socket.gethostname()))
    
    counter = 0

    if rank == 0:
    	data = randomBytes(msgSize)
    	start = MPI.Wtime()

    while counter < 1000:
	if rank == 0:
		reqS = comm.isend(data, dest=1)
		reqS.wait()
		reqR = comm.irecv(dest=1)
      		received = reqR.wait()
		counter += 1
    	elif rank == 1:
       		reqR = comm.irecv(dest=0)
		received = reqR.wait()
		reqS = comm.isend(received, dest=0)
       		reqS.wait()
		counter += 1
	else:
       		print "Expected only two nodes"
    
		
    if rank == 0:
	stop = MPI.Wtime()
	time = stop - start

	processedBitsOneWay = counter * msgSize * 8 * 2
	# bits/s
	capacity = processedBitsOneWay/time
	# Mbit/s
	capacity /= float(1000000)
    	with open('capacityNonblockingNoSHM.csv', 'a') as csvfile:
    		writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
    		writer.writerow(['nonblocking','1nodeNoSHM',msgSize,capacity])
    	print ("msgSize: %d - capacity: %f Mbit/s"%(msgSize,capacity))



def main():
    n = 100
    while n < 10000:    
	measureCapacity(n)
	n += 100

if __name__ == "__main__":
    main()
