import string
lista = []
with open('aoc 3.txt') as topo_file:
    for line in topo_file:
        lista.append(line)
lista2 = [s.strip("\n") for s in lista]        

listaeq = []
l = 0
for l in range(0,len(lista2),3):
    for x in range(len(lista2[l])):
        if lista2[l][x] in lista2[l+1] and lista2[l][x] in lista2[l+2]:
            listaeq.append(lista2[l][x])

mmm = string.ascii_lowercase
xxx = string.ascii_uppercase

aaa=[]
aaa2 = []
for i in mmm:
    aaa.append(i)
for i in xxx:
    aaa2.append(i)
    
def check(lista,aaa,aaa2):
    listafin = []
    cont = 0
    for i in listaeq:
        if i.isupper() == True:
            cont = cont + (aaa2.index(i) + 27)
            listafin.append(aaa2.index(i) + 27)
        elif i.isupper() == False:
            cont = cont + (aaa.index(i) + 1)
            listafin.append(aaa.index(i) + 1)
    
    return sum(listafin)
print(listaeq)
print(check(listaeq,aaa,aaa2))