import numpy as np

def calculate(list):
  # quick check to make sure that the list passed in contains 9 numbers.
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  # shape the list into a 3x3 numpy array
  numArray = np.array(list).reshape(3,3)
  calculationDict = {}
  # call out the methods and the dictionary keys because they are different
  # if we didn't have to pass the tests then we could do away with dict keys 
  # and just use the method names for the keys because they are descriptive enough
  dictKeys = ["mean", "variance", "standard deviation", "max", "min", "sum"] 
  methods = ["mean", "var", "std", "max", "min", "sum"]
  for key, method in zip(dictKeys, methods):
    methodreturnlist = []
    for axis in range(2):
      methodreturnlist.append(eval("numArray.{0}({1})".format(method, str(axis))).tolist())
    methodreturnlist.append(eval("numArray.{0}()".format(method)).tolist())
    calculationDict[key] = methodreturnlist
  return calculationDict