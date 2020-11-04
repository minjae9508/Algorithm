n = list(map(int, input().split()))

ascending = [i for i in range(1,9)]
descending = [i for i in range(8,0,-1)]

if n == ascending:
  print('ascending')
elif n == descending:
  print('descending')
else:
  print('mixed')