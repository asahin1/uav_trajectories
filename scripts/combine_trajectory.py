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


  # txt_file = open('LCP_data/'+args.input+'.txt', 'r')
  # txt_pieces = ['']
  # pieces = 0
  # n_paths = 0
  # file_list = []
  # prev_line = ''
  # while True:
  #   line = txt_file.readline()
  #   if not line:
  #     break
  #   line = line.replace('[','').replace(']','')
  #   if line[1] != '-':
  #     if len(prev_line) != 0:
  #       file_name = 'my_waypoints/'+args.output+"_"+str(n_paths+1)+"_"+str(pieces+1)+'.csv'
  #       csv_file = open(file_name,'w')
  #       csv_file.write(prev_line)
  #       csv_file.write(line)
  #       csv_file.close()
  #       file_list.append(file_name)
  #       pieces += 1
  #     prev_line = line
  #   else:
  #     prev_line = ''
  #     n_paths += 1
  #     pieces = 0
  # txt_file.close()

  # for file in file_list:
  #   data = np.loadtxt(file, delimiter=',', skiprows=0)
  #   data = data * 0.0254; ## inches to meter
  #   data[:,0] -= args.x_off
  #   data[:,1] -= args.y_off
  #   data[:,2] -= args.z_off
  #   data = np.around(data,3)
  #   f = open(file,"w")
  #   writer = csv.writer(f)
  #   for row in data:
  #       writer.writerow(row)
