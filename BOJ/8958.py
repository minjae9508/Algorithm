n = int(input())
m = []
for i in range(n):
  m.append(input())

res = []

for i in m:
  cnt = 0
  sumcnt = 0
  for j in i:
    if j=='O':
      cnt += 1
      sumcnt += cnt
    else:
      cnt = 0
  res.append(sumcnt)

for i in res:
  print(i)