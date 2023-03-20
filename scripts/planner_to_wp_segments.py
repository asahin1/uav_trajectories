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
  n_paths = 0
  file_list = []
  prev_line = ''
  while True:
    line = txt_file.readline()
    if not line:
      break
    line = line.replace('[','').replace(']','')
    if line[1] != '-':
      if len(prev_line) != 0:
        file_name = 'my_waypoints/'+args.output+"_"+str(n_paths+1)+"_"+str(pieces+1)+'.csv'
        csv_file = open(file_name,'w')
        csv_file.write(prev_line)
        csv_file.write(line)
        csv_file.close()
        file_list.append(file_name)
        pieces += 1
      prev_line = line
    else:
      prev_line = ''
      n_paths += 1
      pieces = 0
  txt_file.close()

  for file in file_list:
    data = np.loadtxt(file, delimiter=',', skiprows=0)
    data = data * 0.0254; ## inches to meter
    data[:,0] -= args.x_off
    data[:,1] -= args.y_off
    data[:,2] -= args.z_off
    data = np.around(data,3)
    f = open(file,"w")
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
