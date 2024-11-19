f = open("../be/2.txt", "r")
sorok = f.read().split("\n")
f.close()

# maxR = 12
# maxG = 13
# maxB = 14

# jok = 0
# for i in range(len(sorok)):
#     jatek = sorok[i].split(": ")[1]
#     huzasok = jatek.split("; ")
#     print() 
#     Jo = True
#     for j in range(len(huzasok)):
#         R = 0
#         G = 0
#         B = 0
#         aktHuzas = huzasok[j].split(", ")
#         print(aktHuzas)
#         for k in range(len(aktHuzas)):
#             if aktHuzas[k].split(" ")[1] == "red":
#                 R += int(aktHuzas[k].split(" ")[0])
#             elif aktHuzas[k].split(" ")[1] == "green":
#                 G += int(aktHuzas[k].split(" ")[0])
#             elif aktHuzas[k].split(" ")[1] == "blue":
#                 B += int(aktHuzas[k].split(" ")[0])
#         print(R, G, B)
#         if R > maxR or G > maxG or B > maxB:
#             Jo = False
#     if Jo:
#         jok += (i+1)

# print(jok)            

szorzatok = []
for i in range(len(sorok)):
    jatek = sorok[i].split(": ")[1]
    huzasok = jatek.split("; ")
    print() 

    R = 0
    G = 0
    B = 0
    for j in range(len(huzasok)):
        aktHuzas = huzasok[j].split(", ")
        print(aktHuzas)
        for k in range(len(aktHuzas)):
            if aktHuzas[k].split(" ")[1] == "red" and int(aktHuzas[k].split(" ")[0]) > R:
                R = int(aktHuzas[k].split(" ")[0])
            elif aktHuzas[k].split(" ")[1] == "green" and int(aktHuzas[k].split(" ")[0]) > G:
                G = int(aktHuzas[k].split(" ")[0])
            elif aktHuzas[k].split(" ")[1] == "blue" and int(aktHuzas[k].split(" ")[0]) > B:
                B = int(aktHuzas[k].split(" ")[0])
            print(R, G, B)
    szorzatok.append(R*G*B)

s = 0
for szorzat in szorzatok:
    s += szorzat

print(len(szorzatok), s)