
def read2d(input_binary):
  
  # Initialise 2D representation
  counter = []
  for i in range(256):
    lst = []
    for j in range(256):
      lst.append(0)
  
    counter.append(lst)

  # Fill 2D representation
  with open(input_binary, 'rb') as bin_file:
    byte = bin_file.read(2)
    while byte:
      if len(byte) == 2:
        b, c = byte 
        counter[b][c] += 1

      byte = bin_file.read(2)
  
  return counter
