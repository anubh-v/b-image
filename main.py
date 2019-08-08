import read
from gen_heatmap import gen_heatmap

import sys

def read_and_generate(input_binary, pic_title):
  two_dim_representation = read.read2d(input_binary)
  
  # Generate heatmap using 2D representation
  gen_heatmap(two_dim_representation, pic_title)

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python main.py [input_binary] [pic_title]")
    sys.exit(1)
  
  input_binary = sys.argv[1]
  pic_title = sys.argv[2]
  read_and_generate(input_binary, pic_title)

