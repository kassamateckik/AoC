f = open("../be/1.txt", "r")
sorok = f.read().split("\n")
f.close()


# s = 0
# for adat in sorok:
#     szamjegyek = []
#     for karakter in adat:
#         if karakter.isnumeric() and len(szamjegyek) == 0:
#             szamjegyek.append(int(karakter))
#             utolso = int(karakter)
#         elif karakter.isnumeric():
#             utolso = int(karakter)
#     szamjegyek.append(utolso)
#     s += szamjegyek[0]*10 + szamjegyek[1]

# print(s)


s = 0
for adat in sorok:
    szamjegyek = []
    for i in range(len(adat)):
        if adat[i].isnumeric():
            szamjegyek.append(int(adat[i]))
            continue
        if i+2 < len(adat) and adat[i] == "o" and adat[i+1] == "n" and adat[i+2] == "e":
            szamjegyek.append(1)
            continue
        if i+2 < len(adat) and adat[i] == "t" and adat[i+1] == "w" and adat[i+2] == "o":
            szamjegyek.append(2)
            continue
        if i+4 < len(adat) and adat[i] == "t" and adat[i+1] == "h" and adat[i+2] == "r" and adat[i+3] == "e" and adat[i+4] =="e":
            szamjegyek.append(3)
            continue
        if i+3 < len(adat) and adat[i] == "f" and adat[i+1] == "o" and adat[i+2] == "u" and adat[i+3] == "r":
            szamjegyek.append(4)
            continue
        if i+3 < len(adat) and adat[i] == "f" and adat[i+1] == "i" and adat[i+2] == "v" and adat[i+3] == "e":
            szamjegyek.append(5)
            continue
        if i+2 < len(adat) and adat[i] == "s" and adat[i+1] == "i" and adat[i+2] == "x":
            szamjegyek.append(6)
            continue
        if i+4 < len(adat) and adat[i] == "s" and adat[i+1] == "e" and adat[i+2] == "v" and adat[i+3] == "e" and adat[i+4] =="n":
            szamjegyek.append(7)
            continue
        if i+4 < len(adat) and adat[i] == "e" and adat[i+1] == "i" and adat[i+2] == "g" and adat[i+3] == "h" and adat[i+4] =="t":
            szamjegyek.append(8)
            continue
        if i+3 < len(adat) and adat[i] == "n" and adat[i+1] == "i" and adat[i+2] == "n" and adat[i+3] == "e":
            szamjegyek.append(9)
            continue

    s += (szamjegyek[0]*10 + szamjegyek[len(szamjegyek)-1])

print(s)        
