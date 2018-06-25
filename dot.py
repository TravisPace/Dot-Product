def dot(vector01,vector02):
  '''
  This function calculates the dot product of the two vectors.
  '''
  C = [ ]
  #C is an empty list.
  if len(vector01) != len(vector02):
    print('error')
    return None
  #If the lengths of the vectors are not equal to each other, then the algorithim does not compute and returns none.
  for i in range(len(vector01)):
   #For the length of the vector i.
    C.append(vector01[i] * vector02[i])
    #multiplies each element together and creates a list C.
  D = 0
  #A new integer D is made.
  for i in range(len(C)):
    D = D + C[i]
  return D
  #The function then adds the elements in C toghether to get a single integer, D.
  
vector01 = [1,2]
vector02 = [3,4]
print(dot(vector01,vector02))
