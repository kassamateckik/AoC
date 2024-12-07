f = open("../be/6.txt", "r")
be = f.read().split("\n")
f.close()

def csere(adatok, Or, irany):
    if irany == "e":
        adatok[Or["y"]][Or["x"]], adatok[Or["y"]-1][Or["x"]] = adatok[Or["y"]-1][Or["x"]], adatok[Or["y"]][Or["x"]]
        Or["y"] -= 1
    elif irany == "k":
        adatok[Or["y"]][Or["x"]], adatok[Or["y"]][Or["x"]+1] = adatok[Or["y"]][Or["x"]+1], adatok[Or["y"]][Or["x"]]
        Or["x"] += 1
    elif irany == "d":
        adatok[Or["y"]][Or["x"]], adatok[Or["y"]+1][Or["x"]] = adatok[Or["y"]+1][Or["x"]], adatok[Or["y"]][Or["x"]]
        Or["y"] += 1
    elif irany == "n":
        adatok[Or["y"]][Or["x"]], adatok[Or["y"]][Or["x"]-1] = adatok[Or["y"]][Or["x"]-1], adatok[Or["y"]][Or["x"]]
        Or["x"] -= 1

def benne(x, lista):
    i = 0
    while i < len(lista) and not(lista[i] == x):
        i += 1 
    return i < len(lista)

adatok = []
for i in range(len(be)):
    adattag = []
    for j in range(len(be[i])):
        adattag.append(be[i][j])
    adatok.append(adattag)

Or = {
    "x" : -1,
    "y" : -1
} 

for i in range(len(adatok)):
    for j in range(len(adatok[i])):
        if adatok[i][j] == "^":
            Or["x"] = j
            Or["y"] = i

# print(Or["x"], Or["y"])


irany = "e"
voltakmar = [{"x" : Or["x"], "y" : Or["y"]}]
while Or["x"] < len(adatok)-1 and Or["y"] < len(adatok[0])-1 and Or["x"] > 0 and Or["y"] > 0:
    if irany == "e":
        if adatok[Or["y"]-1][Or["x"]] == "#":
            irany = "k"
        else:
            csere(adatok, Or, irany)
            if not benne({"X" : Or["x"], "y" : Or["y"]}, voltakmar):
                voltakmar.append({"X" : Or["x"], "y" : Or["y"]})
    elif irany == "k":
        if adatok[Or["y"]][Or["x"]+1] == "#":
            irany = "d"
        else:
            csere(adatok, Or, irany)
            if not benne({"X" : Or["x"], "y" : Or["y"]}, voltakmar):
                voltakmar.append({"X" : Or["x"], "y" : Or["y"]})
    elif irany == "d":
        if  adatok[Or["y"]+1][Or["x"]] == "#":
            irany = "n"
        else:
            csere(adatok, Or, irany)
            if not benne({"X" : Or["x"], "y" : Or["y"]}, voltakmar):
                voltakmar.append({"X" : Or["x"], "y" : Or["y"]})
    elif irany == "n":
        if adatok[Or["y"]][Or["x"]-1] == "#":
            irany = "e"
        else:
            csere(adatok, Or, irany)
            if not benne({"X" : Or["x"], "y" : Or["y"]}, voltakmar):
                voltakmar.append({"X" : Or["x"], "y" : Or["y"]})

print(Or["x"], Or["y"])
print(len(voltakmar)-1)