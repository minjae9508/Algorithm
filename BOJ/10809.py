n = input()

res = [-1] * 26

for i in set(n):
  res[ord(i)-97] = n.index(i)

for i in res:
  print(i, end=" ")