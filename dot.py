def dot(vector01,vector02):
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
