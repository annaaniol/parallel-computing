Sources: https://github.com/kfigiela/tpr_lab

Nodes used for testing:
- 02 and 03 - as two nodes on the same host,
- 08 and 09 - as two nodes on different hosts,
- 04 - as one multicore node for measurements with and without SHM.

To generate charts:
```
/ex1: gnuplot gnuplot/plotMultipleDelay.plg
/ex1: gnuplot gnuplot/plotMultipleCapacity.plg
```
