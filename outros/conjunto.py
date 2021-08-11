s1 = set(range(3))
s2 = set(range(10,7,-1))
s3 = set(range(2,10,2))

print("S1: ", s1, "\nS2: ", s2, "\nS3: ", s3)

s1s2 = s1.union(s2)
print("União S1 e S2: ", s1s2)
