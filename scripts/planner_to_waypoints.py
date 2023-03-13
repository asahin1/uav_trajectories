#!/usr/bin/env python

import numpy as np
import argparse
import csv

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("input", type=str, help="txt file containing LCP")
  parser.add_argument("output", type=str, help="CSV file containing waypoints for the trajectory")
  parser.add_argument("--x_off", type=float, default=0, help="mocap origin x offset")
  parser.add_argument("--y_off", type=float, default=0, help="mocap origin y offset")
  parser.add_argument("--z_off", type=float, default=0, help="mocap origin z offset")
  args = parser.parse_args()

  txt_file = open('LCP_data/'+args.input+'.txt', 'r')
  txt_pieces = ['']
  pieces = 0
  init_files = []
  while True:
    line = txt_file.readline()
    if not line:
      break
    line = line.replace('[','').replace(']','')
    if line[0] == '-':
      csv_file = open('my_waypoints/'+args.output+str(pieces+1)+'.csv','w')
      for line in txt_pieces[pieces]:
        csv_file.write(line)
      csv_file.close()
      init_files.append('my_waypoints/'+args.output+str(pieces+1)+'.csv')
      pieces += 1
      txt_pieces.append('')
    else:
      txt_pieces[pieces] += (line)
  txt_file.close()

  for file in init_files:
    data = np.loadtxt(file, delimiter=',', skiprows=0)
    data = data * 0.05;
    data[:,0] -= args.x_off
    data[:,1] -= args.y_off
    data[:,2] -= args.z_off
    data = np.around(data,3)
    f = open(file,"w")
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
