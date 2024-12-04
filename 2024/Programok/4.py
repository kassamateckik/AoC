f = open("../be/4.txt", "r")
be = f.read().split("\n")
f.close()

# print(be)

# 1.
# db = 0
# for i in range(len(be)):
#     for j in range(len(be[i])):
#         if be[i][j] == "X":
#             if j < len(be[i])-3 and be[i][j+1] == "M" and be[i][j+2] == "A" and be[i][j+3] == "S":
#                 db += 1 
#             if j >= 3 and be[i][j-1] == "M" and be[i][j-2] == "A" and be[i][j-3] == "S":
#                 db += 1
#             if i < len(be)-3 and be[i+1][j] == "M" and be[i+2][j] == "A" and be[i+3][j] == "S":
#                 db += 1 
#             if i >= 3 and be[i-1][j] == "M" and be[i-2][j] == "A" and be[i-3][j] == "S":
#                 db += 1 
#             if i < len(be)-3 and j < len(be[i])-3 and be[i+1][j+1] == "M" and be[i+2][j+2] == "A" and be[i+3][j+3] == "S":
#                 db += 1 
#             if i < len(be)-3 and j >= 3 and be[i+1][j-1] == "M" and be[i+2][j-2] == "A" and be[i+3][j-3] == "S":
#                 db += 1 
#             if j < len(be[i])-3 and i >= 3 and be[i-1][j+1] == "M" and be[i-2][j+2] == "A" and be[i-3][j+3] == "S":
#                 db += 1 
#             if j >= 3 and i >= 3 and be[i-1][j-1] == "M" and be[i-2][j-2] == "A" and be[i-3][j-3] == "S":
#                 db += 1 

# print(db)

# 2.

db = 0
for i in range(len(be)):
    for j in range(len(be[i])):
        if i >= 1 and j >= 1 and i< len(be)-1 and j < len(be[i])-1 and be[i][j] == "A":
            if be[i-1][j-1] == "M" and be[i+1][j+1] == "S":
                if (be[i-1][j+1] == "M" and be[i+1][j-1] == "S") or (be[i+1][j-1] == "M" and be[i-1][j+1] == "S"):
                    db += 1
            if be[i+1][j+1] == "M" and be[i-1][j-1] == "S":
                if (be[i-1][j+1] == "M" and be[i+1][j-1] == "S") or (be[i+1][j-1] == "M" and be[i-1][j+1] == "S"):
                    db += 1
        
print(db)