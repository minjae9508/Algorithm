n = []
for i in range(10):
  n.append(int(input()))
  
res = []
for i in n:
  res.append(i%42)

print(len(set(res)))