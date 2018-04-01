printf "pi,time,processors,points" >> ./results/scalable.csv
printf "pi,time,processors,points" >> ./results/nonscalable.csv
printf "points,min_time" >> ./results/sequence.csv
printf "\n" >> ./results/scalable.csv
printf "\n" >> ./results/nonscalable.csv
printf "\n" >> ./results/sequence.csv

for NUMBER_OF_POINTS in 1000000 50000000 100000000
do
	python ./scripts/sequence.py $NUMBER_OF_POINTS >> ./results/sequence.csv
	for NUMBER_OF_PROC in {2..8}
	do
		mpiexec -machinefile ./allnodes -np $NUMBER_OF_PROC ./scripts/parallel.py scalable $NUMBER_OF_POINTS >> ./results/scalable.csv
		mpiexec -machinefile ./allnodes -np $NUMBER_OF_PROC ./scripts/parallel.py nonscalable $NUMBER_OF_POINTS >> ./results/nonscalable.csv
		echo "$NUMBER_OF_POINTS points - done for $NUMBER_OF_PROC processors"
	done
done
