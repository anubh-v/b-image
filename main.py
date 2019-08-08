from gen_heatmap import gen_heatmap
import sys

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python main.py [input_binary] [pic_title]")
    sys.exit(1)
  
  input_binary = sys.argv[1]
  pic_title = sys.argv[2]
  read_and_generate(input_binary, pic_title)

def read_and_generate(input_binary, pic_title):
  
  # Initialise 2D representation
  counter = []
  for i in range(256):
    lst = []
    for j in range(256):
      lst.append(0)
  
    counter.append(lst)

  # Fill 2D representation
  with open(input_file, 'rb') as bin_file:
    byte = bin_file.read(2)
    while byte:
      if len(byte) == 2:
        b, c = byte 
        counter[b][c] += 1

    byte = bin_file.read(2)
  
  # Generate heatmap using 2D representation
  gen_heatmap(counter, sys.argv[2])
