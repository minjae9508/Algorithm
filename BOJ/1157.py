from collections import Counter

n = Counter(list(input().upper()))

m = dict(n)

key_list = m.keys()
value_list = m.values()

t = list(map(lambda a,b: (a,b), key_list, value_list))

k = list(sorted(t, key=lambda x: x[1], reverse=True))

if len(k) == 1:
  print(k[0][0])
else:
  b = k[0][1]
  if b == k[1][1]:
    print("?")
  else:
    print(k[0][0])