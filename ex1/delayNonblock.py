#!/usr/bin/env python
from mpi4py import MPI
import random
import csv
import sys
import socket

def measureDelay():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    # print("my rank is: %d, at node %s"%(comm.rank, socket.gethostname()))
    
    counter = 0
    packageDelay = {}

    if rank == 0:
    	data = 0
    	start = MPI.Wtime()

    while counter < 1000:
        comm.barrier()
	if rank == 0:
		start = MPI.Wtime()
		reqS = comm.isend(data, dest=1)
		reqS.wait()
		reqR = comm.irecv(dest=1)
      		received = reqR.wait()
		stop = MPI.Wtime()
		counter += 1
		delay = (stop-start)*1000
		packageDelay.update({counter: delay})
    	elif rank == 1:
       		reqR = comm.irecv(dest=0)
		received = reqR.wait()
		reqS = comm.isend(received, dest=0)
       		reqS.wait()
		counter += 1
	else:
       		print "Expected only two nodes"
    
		
    if rank == 0:
	with open('delayNonblockingTwoNodes.csv', 'a') as csvfile:
    		writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for package, delay in packageDelay.items():
    			writer.writerow(['nonblocking','2nodes',package,delay])
    	



def main():
    measureDelay()

if __name__ == "__main__":
    main()
