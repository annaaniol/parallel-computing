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
        comm.barrier()
	if rank == 0:
		comm.send(data, dest=1)
		received = comm.recv(source=1)
      		counter += 1
    	elif rank == 1:
       		received = comm.recv(source=0)
		comm.send(received, dest=0)
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
    	with open('capacityBlockingOneCore.csv', 'a') as csvfile:
    		writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
    		writer.writerow(['blocking','1nodeOneCore',msgSize,capacity])
    	print ("msgSize: %d - capacity: %f Mbit/s"%(msgSize,capacity))



def main():
    n = 100
    while n < 10000:    
	measureCapacity(n)
	n += 100

if __name__ == "__main__":
    main()
