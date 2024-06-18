import numpy as np

a = np.array([1,2])
b = np.array([3,4])

dot = 0
for e, f in zip(a, b):
  dot += e*f

#print(dot) ... 11

dot = 0
dot = np.sum(a * b)

#print(dot) ... 11

dot = 0
dot = (a * b).sum()

#print(dot) ... 11

dot = 0
dot = np.dot(a, b)

#print(dot) ... 11

dot = 0
dot = a.dot(b)

#print(dot) ... 11

dot = 0
dot = b.dot(a)

#print(dot) ... 11

dot = 0
dot = a @ b

#print(dot) ... 11

amag = 0
amag = np.sqrt((a * a).sum())

#print(amag) ... 2.23606797749979

amag = 0
amag = np.linalg.norm(a)

#print(amag) ... 2.23606797749979

cosangle = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))

#print(cosangle) ... 0.9838699100999074

angle = np.arccos(cosangle)

#print(angle) ... 0.17985349979247847
