# Tables
Functions = []

# placement (don't you give a crap about this.)
def args(y):
  c = 0
  for x in y:
    c = c + 1
  return c

# functions
def Print(string):
  print(string)

# script
pos = args(Functions) + 1
Functions.insert(pos, Print)

for x in Functions:
  x("NICE!")
