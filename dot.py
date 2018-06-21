def dot(vector01,vector02):
  '''
  This function calculates the dot product of the two vectors. C is an empty list. If the lengths of the vectors are not equal to each
  other, then the algorithim does not compute and returns none. For teh length of the vector, this multiplies each element together
  and returns C as a list. A new integer, D, is made. The function then adds the elements in C toghether to get a single integer.
  '''
  C = [ ]
  if len(vector01) != len(vector02):
    print('error')
    return None
  for i in range(len(vector01)):
    C.append(vector01[i] * vector02[i])
  D = 0
  for i in range(len(C)):
    D = D + C[i]
  return D

vector01 = [1,2]
vector02 = [3,4]
print(dot(vector01,vector02))
