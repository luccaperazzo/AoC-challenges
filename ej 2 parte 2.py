#parametros
C = "Scissors"
A = "Rock"
B = "Paper"

Z=  "win"
X = "lose"
Y = "draw"

Z = 3
X = 1
Y = 2

lose = 0
draw = 3
won = 6
points = 0

#lista inicial
lista = []
with open('aoc 2.txt') as topo_file:
    for line in topo_file:
        lista.append(line)
        
#lista final        
lista2 = [s.strip("\n") for s in lista]
print(lista2)


for i in lista2:
    if i == "C Y":
        points = points + draw + 3
    elif i == "C X":
        points = points + lose + 2
    elif i == "C Z":
        points = points + won + 1
    elif i == "A Z":
        points = points + won + 2
    elif i == "A X":
        points = points + lose + 3
    elif i == "A Y":
        points = points + draw + 1
    elif i == "B Z":
        points = points + won + 3
    elif i == "B X":
        points = points + lose + 1
    elif i == "B Y":
        points = points + draw + 2
                
print(points)           
        