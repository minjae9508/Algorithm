n = int(input())
score = list(map(int, input().split()))

m = max(score)

sumlist = []
for a in score:
  sumlist.append(a/m*100)

print(sum(sumlist)/n)

    