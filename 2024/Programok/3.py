f = open("../be/3.txt", "r")
be = f.read()
f.close()

S = 0
szabad = True
for i in range(len(be)):

    if szabad:
        if be[i] == "m" and be[i+1] == "u" and be[i+2] == "l" and be[i+3] == "(" and be[i+4].isnumeric(): 
            a = ""
            b = ""
            k = i+4
            while be[k].isnumeric():
                a += be[k]
                k += 1
            if be[k] == "," and be[k+1].isnumeric():
                j = k+1
                while be[j].isnumeric():
                    b += be[j]
                    j += 1
                if be[j] == ")":
                    # print(a, b, int(a) * int(b))
                    S += (int(a) * int(b))
    if be[i] == "d" and be[i+1] == "o" and be[i+2] == "n" and be[i+3] == "'" and be[i+4] == "t" and be[i+5] == "(" and be[i+6] == ")":
        szabad = False
    if be[i] == "d" and be[i+1] == "o" and be[i+2] == "(" and be[i+3] == ")":
        szabad = True

print(S)



