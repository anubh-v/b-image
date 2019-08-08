from gen_heatmap import gen_heatmap

import sys

input_file = sys.argv[1]

counter = []
for i in range(256):
  lst = []
  for j in range(256):
    lst.append(0)
  
  counter.append(lst)

with open(input_file, 'rb') as bin_file:
  byte = bin_file.read(2)
  while byte:
    if len(byte) == 2:
      b, c = byte 
      counter[b][c] += 1

    byte = bin_file.read(2)

gen_heatmap(counter, sys.argv[2])
