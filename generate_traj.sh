#!/bin/bash
while getopts i:o:n: flag
do
    case "${flag}" in
        i) input_name=${OPTARG};;
        o) output_name=${OPTARG};;
        n) n_segments=${OPTARG};;
    esac
done

echo "input name: $input_name";
echo "output name: $output_name";
echo "num segments: $n_segments";

for i in $(seq 1 1 $n_segments)
do
    echo "./build/genTrajectory -i my_waypoints/${input_name}_${i}.csv -o my_trajectories/${output_name}_${i}.csv --v_max 0.5 --a_max 0.5"
    ./build/genTrajectory -i my_waypoints/${input_name}_${i}.csv -o my_trajectories/${output_name}_${i}.csv --v_max 0.5 --a_max 0.5
done