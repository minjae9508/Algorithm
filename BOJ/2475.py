n = list(map(int, input().split()))
sumlist = 0
for i in n:
  sumlist += i*i

print(sumlist%10)