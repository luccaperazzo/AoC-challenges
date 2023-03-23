import sys
lista = []
with open('aoc ej 1 .txt') as topo_file:
    for line in topo_file:
        lista.append(line)
        
        
xd = " "
lista2 = [s.strip("\n") for s in lista]
lista3= []
for i in lista2:
    if i == "":
        i = "0000"
    lista3.append(i)
# int list
a = list(map(int, lista3))
indices = [i for i, x in enumerate(a) if x == 0000]
p = 0
print(indices)
third = second = first = -sys.maxsize
print(a[2216])
for i in range(len(a)-11):
    if a[i] == 0:
        if sum(a[indices[p]:indices[p+1]]) > first:
            third = second
            second = first
            first = sum(a[indices[p]:indices[p+1]])
            p = p + 1       
        elif sum(a[indices[p]:indices[p+1]]) > second:
            third = second
            second = sum(a[indices[p]:indices[p+1]])
            p = p + 1       
        elif sum(a[indices[p]:indices[p+1]]) > third:
            third = sum(a[indices[p]:indices[p+1]])
            p = p + 1       
        else:
            p = p + 1
print("Three largest elements are ",first, second, third)
    

    