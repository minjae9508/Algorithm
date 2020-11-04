a, b = input().split()
lista = []
listb = []
resa = ""
resb = ""

for i in range(3):
  lista.append(a[i])
  listb.append(b[i])

lista.reverse()
listb.reverse()


for i in range(3):
  resa += lista[i]
  resb += listb[i]

print(max(int(resa), int(resb)))