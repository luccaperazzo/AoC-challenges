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
p = 0
indices = [i for i, x in enumerate(a) if x == 0000]
xddd = sum(a[0:indices[p]])
for i in range(len(a)):
    if a[i] == 0:
        if sum(a[indices[p]:indices[p+1]]) > xddd:
            xddd = sum(a[indices[p]:indices[p+1]])
            
        else:
            p += 1
print(xddd)
        
    