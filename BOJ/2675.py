n = int(input())
m = []
for i in range(n):
  m.append(list(input().split()))

for i in m:
  for j in i[1]:
    print(j*int(i[0]), end='')
  print()