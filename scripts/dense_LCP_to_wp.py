#!/usr/bin/env python

import numpy as np
import argparse
import csv

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("input", type=str, help="txt file containing LCP")
  parser.add_argument("output", type=str, help="CSV file containing waypoints for the trajectory")
  parser.add_argument("--n_sample", type=int, default=1, help="LCP sampling density")
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
      file_name = 'my_waypoints/'+args.output+'_'+str(pieces+1)+'.csv'
      csv_file = open(file_name,'w')
      for line in txt_pieces[pieces]:
        csv_file.write(line)
      csv_file.close()
      init_files.append(file_name)
      pieces += 1
      txt_pieces.append('')
    else:
      txt_pieces[pieces] += (line)
  txt_file.close()

  pt_prev = None
  for file in init_files:
    data = np.loadtxt(file, delimiter=',', skiprows=0)
    data = data * 0.0254; ## inches to meter
    data[:,0] -= args.x_off
    data[:,1] -= args.y_off
    data[:,2] -= args.z_off
    data = np.around(data,3)
    f = open(file,"w")
    writer = csv.writer(f)
    it = data.shape[0]
    for i in range(0,it-1):
      p1 = data[i,:]
      p2 = data[i+1,:]
      diff = p2-p1
      step = diff/args.n_sample
      for j in range(0,args.n_sample):
        pt = p1 + step*j
        pt = np.around(pt,3)
        if (pt != pt_prev).any():
          writer.writerow(pt)
        pt_prev = pt
    writer.writerow(data[-1,:])
