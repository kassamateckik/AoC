f = open("../be/2.txt", "r")
sorok = f.read().split("\n")
f.close()


def szamma(l):
    for i in range(len(l)):
        l[i] = int(l[i])


# db = 0
# for i in range(len(sorok)):
#     elemek = sorok[i].split(" ")
#     szamma(elemek)

#     k = 0 
#     if elemek[k] < elemek[k+1]:
#         while k < len(elemek)-1 and elemek[k] < elemek[k+1] and abs(elemek[k] - elemek[k+1]) >= 1 and abs(elemek[k] - elemek[k+1]) <= 3:
#             k += 1 
#         safe = not(k < len(elemek)-1)
#     elif elemek[k] > elemek[k+1]:
#         while k < len(elemek)-1 and elemek[k] > elemek[k+1] and abs(elemek[k] - elemek[k+1]) >= 1 and abs(elemek[k] - elemek[k+1]) <= 3:
#             k += 1 
#         safe = not(k < len(elemek)-1)
#     else:
#         safe = False
    
#     if safe:
#         db += 1

# print(db)


db = 0
for i in range(len(sorok)):
    elemek = sorok[i].split(" ")
    szamma(elemek)

    hiba = 0
    if elemek[0] < elemek[1]:
        for k in range(len(elemek)-1):
            if elemek[k] >= elemek[k+1] or abs(elemek[k] - elemek[k+1]) < 1 or abs(elemek[k] - elemek[k+1]) > 3:
                hiba += 1

    elif elemek[0] > elemek[1]:
        for k in range(len(elemek)-1):
            if elemek[k] <= elemek[k+1] or abs(elemek[k] - elemek[k+1]) < 1 or abs(elemek[k] - elemek[k+1]) > 3:
                hiba += 1

    elif elemek[0] == elemek[1]:
        hiba += 1
        if elemek[1] < elemek[2]:
            for k in range(len(elemek)-1):
                if elemek[k] >= elemek[k+1] or abs(elemek[k] - elemek[k+1]) < 1 or abs(elemek[k] - elemek[k+1]) > 3:
                    hiba += 1

        elif elemek[1] > elemek[2]:
            for k in range(len(elemek)-1):
                if elemek[k] <= elemek[k+1] or abs(elemek[k] - elemek[k+1]) < 1 or abs(elemek[k] - elemek[k+1]) > 3:
                    hiba += 1

    if hiba <= 1:
        db += 1

print(db)