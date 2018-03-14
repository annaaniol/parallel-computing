#!/usr/bin/env python
from mpi4py import MPI
import random
import csv
import sys
import socket
from utils import *

def writeToFile(packageDelay, configType):
    filename = resultsDelayDir+configType+'Nonblocking'+resultsFormat

    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for package, delay in packageDelay.items():
            writer.writerow(['nonblocking',configType,package,delay])

def measureDelay(configType):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    counter = 0
    packageDelay = {}

    comm.barrier()

    if rank == 0:
        data = 0
        start = MPI.Wtime()

    while counter < 1000:
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
        writeToFile(packageDelay, configType)

def main():
    configType = sys.argv[1]
    measureDelay(configType)

if __name__ == "__main__":
    main()
