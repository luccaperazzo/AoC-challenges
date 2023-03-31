import re
lista = []
with open('aoc 5.txt') as topo_file:
    for line in topo_file:
        lista.append(line)
lista2 = [s.strip("\n") for s in lista]
            
listanum = [int(word) for item in lista2 for word in item.split() if word.isdigit()]

tabla = {
  1: ["[S]","[C]","[V]","[N]"],
  2: ["[Z]","[M]","[J]","[H]","[N]","[S]"],
  3: ["[M]","[C]","[T]","[G]","[J]","[N]","[D]"],
  4: ["[M]","[C]","[T]","[G]","[J]","[N]","[M]"],
  5: ["[P]","[F]","[H]"],
  6: ["[C]","[T]","[Z]","[H]","[J]"],
  7: ["[D]","[P]","[R]","[Q]","[F]","[S]","[L]","[Z]"],
  8: ["[C]","[S]","[L]","[H]","[D]","[F]","[P]","[W]"],
  9: ["[D]","[S]","[M]","[P]","[F]","[N]","[G]","[Z]"]
}
listacant = []
listadesde = []
listahacia = []
for i in range(0,len(listanum),3):
    listacant.append(listanum[i])
for i in range(1,len(listanum),3):
    listadesde.append(listanum[i])
for i in range(2,len(listanum),3):
    listahacia.append(listanum[i])
    
    

h = 0
while h < len(listadesde):
    a = tabla[listadesde[h]][-listacant[h]:]
    del tabla[listadesde[h]][-listacant[h]:]
    tabla[listahacia[h]].extend(a)
    h = h + 1
print(tabla)
