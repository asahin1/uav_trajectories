#!/usr/bin/env python

import numpy as np
import argparse
import csv

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("input", type=str, help="input file base name for trajectories")
  parser.add_argument("output", type=str, help="base name for the combined file")
  parser.add_argument("n_segments", type=int, help="number of files to combine")
  args = parser.parse_args()

  out_file = open('my_trajectories/'+args.output+'_combined.csv','w')
  writer = csv.writer(out_file)
  for i in range(1,args.n_segments+1):
    with open('my_trajectories/'+args.input+'_'+str(i)+'.csv','r') as read_obj:
      csv_reader = csv.reader(read_obj)
      header = next(csv_reader)
      if i==1:
        writer.writerow(header)
      for row in csv_reader:
        writer.writerow(row)
