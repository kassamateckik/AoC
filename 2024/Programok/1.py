f = open("../be/1.txt", "r")
sorok = f.read().split("\n")
f.close()

lista1 = []
lista2 = []

def minIdx(l, a):
    mini = a
    for i in range(a, len(l)):
        if l[i] < l[mini]:
            mini = i
    return mini

def csere(l, a, b):
    m = l[a]
    l[a] = l[b]
    l[b] = m

def rendez(l):
    for i in range(len(l)):
        mini = minIdx(l, i)
        csere(l, i, mini)


for i in range(len(sorok)):
    lista1.append(int(sorok[i].split("   ")[0]))
    lista2.append(int(sorok[i].split("   ")[1]))


rendez(lista1)
rendez(lista2)

# 1.

# s = 0
# for i in range(len(lista1)):
#     s += (abs(lista1[i] - lista2[i]))
# print(s)



# 2.
s = 0
for i in range(len(lista1)):
    db = 0
    for k in range(len(lista2)):
        if lista1[i] == lista2[k]:
            db += 1
    s += lista1[i] * db
print(s)