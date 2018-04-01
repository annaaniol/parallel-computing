#### To run the non-scalable program on 8 processors with 1000000 points in total:

`mpiexec -machinefile ./allnodes -np 8 ./parallel.py nonscalable 1000000`

#### To run the scalable program on 4 processors with 1000000 points per processor:

`mpiexec -machinefile ./allnodes -np 4 ./parallel.py scalable 1000000`

#### To run all computations:
`./run.sh`

#### To plot all charts:
`gnuplot gnuplot/scripts/plot.plg `
