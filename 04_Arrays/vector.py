# Program 'vector' uses 'vectormath' module perform vector operations
# Bonga Njamela [NJMLUN002]
# 02/06/20

import vectormaths

# This section A of code converts the string values of the components of A
# into a list of integer values of the components of A
vectorA_str = input("Enter vector A:\n")
vectorA_list = list(vectorA_str)
vectorA_list.remove(" ")
vectorA_list.remove(" ")
vector_A = []
for i in range(len(vectorA_list)):
    comp_A = int(vectorA_list[i])
    vector_A.append(comp_A)
    vector_A = vector_A
# END of section A

# This section B of code converts the string values of the components of B
# into a list of integer values of the components of B
vectorB_str = input("Enter vector B:\n")
vectorB_list = list(vectorB_str)
vectorB_list.remove(" ")
vectorB_list.remove(" ")
vector_B = []
for i in range(len(vectorB_list)):
    comp_B = int(vectorB_list[i])
    vector_B.append(comp_B)
    vector_B = vector_B
# END of section B

vector_op = input("Select a calculation to perform. Enter '+', '.' or '|':\n")

if vector_op == "+":
    print("A+B =", vectormaths.vector_sum(vector_A, vector_B))
elif vector_op == ".":
    print("A.B =", vectormaths.vector_product(vector_A, vector_B))
elif vector_op == "|":
    print("|A| =", "{:.2f}".format(vectormaths.vector_norm(vector_A)))
    print("|B| =", "{:.2f}".format(vectormaths.vector_norm(vector_B)))
else:
    print("Selection not recognised.")