# print this pattern
# # # #
# # # #
# # # #
# # # #

for j in range(4):
    for i in range(4):
        print("# ", end="")
    print()

#Print this pattern
#
# #
# # #
# # # #

for j in range(4):
    for i in range(j+1):
        print("# ", end="")
    print()

#Print this pattern
# # # #
# # #
# #
#


for k in range(4):
    for l in range(4-k):
        print("# ", end="")

    print()

#or the same thing can be done is different way
m=4
for k in range(4):
    for l in range(m):
        print("# ", end="")
    m-=1

    print()
