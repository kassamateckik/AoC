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

    if jo:
        jok.append(oldal)
    else:
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


for i in range(len(rosszak)):
    for j in range(len(szabalyok)):
        a = szabalyok[j].split("|")[0]
        b = szabalyok[j].split("|")[1]
        for k in range(len(rosszak[i])):
            for h in range(k, len(rosszak[i])):
                if rosszak[i][k] == a and rosszak[i][h] == b and h <= k:
                    csere(rosszak[i], k, h)
                    
s = 0 
for i in range(len(rosszak)):
    s += int(rosszak[i][int((len(rosszak[i])-1)/2)])

# 4937 - low
# 5013 - high
print(s)