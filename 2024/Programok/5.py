f = open("../be/5a.txt", "r")
szabalyok = f.read().split("\n")
f.close()

f = open("../be/5b.txt", "r")
oldalak = f.read().split("\n")
f.close()

jok = []
rosszak = []
for i in range(len(oldalak)):
    oldal = oldalak[i].split(",")
    jo = True
    jo2 =False
    for k in range(len(szabalyok)):
        a = szabalyok[k].split("|")[0]
        b = szabalyok[k].split("|")[1]
        j = 0
        while j < len(oldal) and not(oldal[j] == a):
            j += 1
        h = 0
        while h < len(oldal) and not(oldal[h] == b):
            h += 1
        if j < len(oldal) and h < len(oldal) and h < j:
            jo = False
            jo2 = True
            

    if jo:
        jok.append(oldal)
    if jo2:
        rosszak.append(oldal)

# print(jok)

# s = 0 
# for i in range(len(jok)):
#     s += int(jok[i][int((len(jok[i])-1)/2)])

# print(s)

def csere(l, i ,j):
    a = l[i]
    l[i] = l[j]
    l[j] = a

# print(rosszak)

jok2 = []
for i in range(len(rosszak)):
    valtozott = False
    for j in range(len(szabalyok)):
        a = szabalyok[j].split("|")[0]
        b = szabalyok[j].split("|")[1]
        for k in range(len(rosszak[i])):
            for h in range(len(rosszak[i])):
                while rosszak[i][k] == a and rosszak[i][h] == b and h <= k:
                    # print("asd")
                    csere(rosszak[i], k, h)
                    valtozott = True
    if valtozott:
        jok2.append(rosszak[i])

# print(jok2)
      
s = 0 
for i in range(len(jok2)):
    s += int(jok2[i][int((len(jok2[i])-1)/2)])

# 4937 - low
# 5013 - high
print(s)