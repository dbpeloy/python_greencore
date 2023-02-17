
from itertools import permutations

n = 1234
print(["".join(x) for x in permutations(str(n))]) 
