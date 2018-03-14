import os
from utils import *

def main():
    os.popen('mkdir -p results').read()
    os.popen('mkdir -p results/capacity').read()
    os.popen('mkdir -p results/delay').read()

   os.popen('rm -f results/capacity/*').read()
   os.popen('rm -f results/delay/*').read()

   os.popen('mpiexec -machinefile ./allnodes/' + oneNode
       + ' -np 2 ./scripts/capacityBlock.py ' + oneNode).read()
   os.popen('mpiexec -machinefile ./allnodes/' + twoNodesSameHost
       + ' -np 2 ./scripts/capacityBlock.py ' + twoNodesSameHost).read()
   os.popen('mpiexec -machinefile ./allnodes/' + twoNodesDifferentHost
       + ' -np 2 ./scripts/capacityBlock.py ' + twoNodesDifferentHost).read()

    os.popen('mpiexec -machinefile ./allnodes/' + oneNode
        + ' -np 2 ./scripts/capacityNonblock.py ' + oneNode).read()
    os.popen('mpiexec -machinefile ./allnodes/' + twoNodesSameHost
        + ' -np 2 ./scripts/capacityNonblock.py ' + twoNodesSameHost).read()
    os.popen('mpiexec -machinefile ./allnodes/' + twoNodesDifferentHost
        + ' -np 2 ./scripts/capacityNonblock.py ' + twoNodesDifferentHost).read()

    os.popen('mpiexec -machinefile ./allnodes/' + oneNode
        + ' -np 2 ./scripts/delayBlock.py ' + oneNode).read()
    os.popen('mpiexec -machinefile ./allnodes/' + twoNodesSameHost
        + ' -np 2 ./scripts/delayBlock.py ' + twoNodesSameHost).read()
    os.popen('mpiexec -machinefile ./allnodes/' + twoNodesDifferentHost
        + ' -np 2 ./scripts/delayBlock.py ' + twoNodesDifferentHost).read()

    os.popen('mpiexec -machinefile ./allnodes/' + oneNode
        + ' -np 2 ./scripts/delayNonblock.py ' + oneNode).read()
    os.popen('mpiexec -machinefile ./allnodes/' + twoNodesSameHost
        + ' -np 2 ./scripts/delayNonblock.py ' + twoNodesSameHost).read()
    os.popen('mpiexec -machinefile ./allnodes/' + twoNodesDifferentHost
        + ' -np 2 ./scripts/delayNonblock.py ' + twoNodesDifferentHost).read()

if __name__ == "__main__":
    main()
