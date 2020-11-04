result = 1
for i in range(3):
  n = int(input())
  result *= n

st = str(result)
cnt = [0] * 10

for i in set(st):
  cnt[int(i)] = st.count(i)

for i in cnt:
  print(i)


