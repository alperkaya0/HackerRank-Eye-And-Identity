import numpy
numpy.set_printoptions(legacy='1.13')

inp = input()
inp = inp.split(" ")

for x in range(len(inp)):
    inp[x] = int(inp[x])

print(numpy.eye(inp[0],inp[1]))
