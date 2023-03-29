lista = []
with open('aoc4.txt') as topo_file:
    for line in topo_file:
        lista.append(line)
lista2 = [s.strip("\n") for s in lista]

newlist = []
for word in lista2:
    word = word.split(",")
    newlist.extend(word)  

#lista final
listafinal = []
for word in newlist:
    word = word.split("-")
    listafinal.extend(word)  

laposta = list(map(int, listafinal))
print(laposta)
counter = 0
for i in range(0,len(laposta),4):
    set1 = set(range(laposta[i],laposta[i+1]+1))
    set2 = set(range(laposta[i+2],laposta[i+3]+1))
    if not set1.isdisjoint(set2) or not set2.isdisjoint(set1):
        counter += 1
print(counter)