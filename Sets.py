# sets only have values NO KEYS
A = {40,-2,20,13}
B = {30,80,90,13}
print("A")
print(A)
A.add(24)
print("A with 24 added")
print(A)
# you never know which order the values are going to appear on
print("Sorted a")
print(sorted(A))
# the sort method sorts the values but converts the set into a list

W = [20,70,99,20,4,9,99,30,30]
S = set(W)
print("S")
print(S)
# we can convert lists to sets in order to remove duplicate values,
# because sets can only contain unique values

A.discard(40)
print("A with 40 discarded")
print(A)
A.remove(-2)
# If you use the remove method and the number is not contained in
# the set, python will spit an error whereas when you use discard
# it wont

Z = A|B
print("Z")
print(Z)
# combines both sets (data bases) and removes any repeated values

X = A&B
print("X")
print(X)
# compares both sets (data bases) and shows which elements are repeated

K = A-B
print("K")
print(K)
# removes any number from the first set that exists in the second one
# and will print the remaining ones in the first set

V = A ^ B
print("A and B XOR (exclusive of)")
print(V)
# this operation deletes any value that has been repeated and combines
# both sets

U = A.issubset(B)
print("If A is subset of B")
print(U)
# checks if the values of one set are included in the other one, for
# it to be true ALL OF THEM have to be included


            #SETS AND THEIR OPPERATIONS AND CORRESPONDING FUNCTIONS
            # |  - Union                                  .union()
            # &  - Intersection                           .intersection()
            # -  - Difference                             .difference()
            # ^  - XOR or eXclusive OR                    .__xor__()
