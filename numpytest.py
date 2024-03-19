import numpy as np

n = np.random.randint(1, 20)
randomlist = []
for i in range (1000000):
    n = np.random.randint(1,20)
    randomlist.append(n)
#
print("randomlist:", randomlist)
