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

