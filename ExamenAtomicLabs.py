# Examen Atomic Labs 
# Roberto Narvaez Hernandez
import numpy as np
import random
import csv

# Funcion checa si el zombie pasa junto a un humano
def juntoHum (opciones):
    pos = []
    for i in range(8):
        if Map[opciones[i,0],opciones[i,1]] == 1:
            pos = np.append(pos,i)
    return pos

# Funcion Zombie Avanza
def ZombieA(ubi,indiceZ):
    # Creamos copia del mapa
    mapt = np.copy(Map)
    mapt[15:19,19] = -1
    # Casillas disponibles
    cercanos = np.array([[ubi[0]-1,ubi[1]-1],[ubi[0]-1,ubi[1]],[ubi[0]-1,ubi[1]+1],[ubi[0],ubi[1]-1],
                        [ubi[0],ubi[1]+1],[ubi[0]+1,ubi[1]-1],[ubi[0]+1,ubi[1]],[ubi[0]+1,ubi[1]+1]])
    for i in range(4):
        # Bloqueamos la casilla actual para que no regrese a ella 
        mapt[ubi[0],ubi[1]] = 7
        # Elegimos nueva posicion alazar
        # Probabilidades 
        p = np.zeros(8)
        # Encontramos casillas disponibles
        for i in range(8):
            if mapt[cercanos[i,0],cercanos[i,1]] == 0:
                p[i] = 1
        # Elejimos aleatoriamente
        if np.all((p == 0)):
            break
        norma = np.linalg.norm(p,ord=1)
        p = p/norma
        rand = np.random.choice(np.arange(8),1,p=p)
        ubi = cercanos[rand[0],:]
        # print("El zombie se movio a :",ubi[0],ubi[1])
        # Casillas disponibles
        cercanos = np.array([[ubi[0]-1,ubi[1]-1],[ubi[0]-1,ubi[1]],[ubi[0]-1,ubi[1]+1],[ubi[0],ubi[1]-1],
                            [ubi[0],ubi[1]+1],[ubi[0]+1,ubi[1]-1],[ubi[0]+1,ubi[1]],[ubi[0]+1,ubi[1]+1]])
        # Si pasa junto a un humano lo vuelve zombie
        for n in juntoHum(cercanos):
            N = int(n)
            Map[cercanos[N,0],cercanos[N,1]] = 2
            indice = np.where((Agentes[:,0] == cercanos[N,0]) & (Agentes[:,1] == cercanos[N,1]))
            print("El humano", Nombres[Agentes[indice[0][0],3]], "ha sido infectado en la casilla x =", cercanos[N,0], 
                  "y =", cercanos[N,1],"por el Zombie",Nombres[Agentes[indiceZ,3]])
            Agentes[indice[0][0],2] = 2
    return ubi

# Funcion checa si humano pasa junto a zombie 
def juntoZom(opciones):
    for i in range(8):
        if Map[opciones[i,0],opciones[i,1]] == 5:
            indice = np.where((Agentes[:,0] == opciones[i,0]) & (Agentes[:,1] == opciones[i,1]))
            res = indice[0][0] + 1
            return res
    return 0

# Funcion humano avanza 
def HumanoA(ubi,indice):
    # Creamos copia del mapa
    mapt = np.copy(Map)
    # pesos para probabilidades
    ch = 0.1
    m = 0.75
    g = 2
    # Casillas disponibles
    cercanos = np.array([[ubi[0]-1,ubi[1]-1],[ubi[0]-1,ubi[1]],[ubi[0]-1,ubi[1]+1],[ubi[0],ubi[1]-1],
                        [ubi[0],ubi[1]+1],[ubi[0]+1,ubi[1]-1],[ubi[0]+1,ubi[1]],[ubi[0]+1,ubi[1]+1]])
    for i in range(2):
    # Bloqueamos la casilla actual para que no regrese a ella 
        mapt[ubi[0],ubi[1]] = 7
    # Elegimos a que casilla nos vamos a mover
        # Probabilidades 
        p = np.zeros(8)
        # Encontramos casillas disponibles
        for i in range(8):
            if mapt[cercanos[i,0],cercanos[i,1]] == 0:
                p[i] = 1
        # Damos mas peso a posibilidades favorables
        if ubi[0] <= 10:
            if ubi[1] <= 8:
                mov = np.array([ch,ch,ch,m,g,m,g,g])
            elif ((ubi[1] >= 9) and (ubi[1] <= 12)):
                mov = np.array([ch,ch,ch,g,g,g,g,g])
            else:
                mov = np.array([ch,ch,ch,g,m,g,g,m])
        elif ((ubi[0] >= 11) and (ubi[0] <= 14)):
            mov = np.array([ch,m,m,ch,g,ch,g,g])
        else:
            mov = np.array([ch,m,g,ch,g,ch,m,g])
        p = p*mov
        # Elegimos a donde se va a mover
        if np.all((p == 0)):
            break
        norma = np.linalg.norm(p,ord=1)
        p = p/norma
        rand = np.random.choice(np.arange(8),1,p=p)
        ubi = cercanos[rand[0],:]
        #print("El humano se movio a :",ubi[0],ubi[1])
    # Casillas disponibles
        cercanos = np.array([[ubi[0]-1,ubi[1]-1],[ubi[0]-1,ubi[1]],[ubi[0]-1,ubi[1]+1],[ubi[0],ubi[1]-1],
                            [ubi[0],ubi[1]+1],[ubi[0]+1,ubi[1]-1],[ubi[0]+1,ubi[1]],[ubi[0]+1,ubi[1]+1]])
    # Checar si llego a la salida 
        if ubi[1] == 19:
            print("El humano", Nombres[Agentes[indice,3]], "salvado en la casilla x = ", ubi[0], "y =", ubi[1])
            Agentes[indice,2] = 10
            break
    # Checar si esta junto a un zombie
        indiceZ = juntoZom(cercanos)
        if indiceZ:
            print("El humano", Nombres[Agentes[indice,3]], "ha sido infectado en x =", ubi[0], "y =", ubi[1],
                  "por el Zombie",Nombres[Agentes[indiceZ-1,3]])
            Agentes[indice,2] = 2
            break
    return ubi

# Hacemos el mapa
Map = np.zeros([20,20])
Map[0:,[0,19]] = -1
Map[[0,19],0:] = -1
Map[10,0:8] = -1
Map[10,12:] = -1
Map[[4,12,16],2:8] = -1
Map[4,10:17] = -1
Map[5:8,13] = -1
Map[12:16,[12,16]] = -1
Map[15:19,19] = 0

# Array de agentes (x,y,1-persona 2-4 transformando 5-zombie)
Agentes = np.array([[1,9,1],[3,3,1],[3,6,1],[3,11,1],[3,15,1],[5,4,1],[6,15,1],[7,2,1],[7,7,1],[8,3,1],[8,17,1],[9,11,1],
                   [12,13,1],[13,3,1],[13,17,1],[14,6,1],[15,10,1],[17,3,1],[17,7,1],[17,13,1],[1,0,5],[1,0,5]])
Agentes = np.append(Agentes,np.reshape(np.arange(22),(22,1)),axis=1)
Nombres = ('Fernando','Enrique','Gerardo','Diego','Andres','Liliana','Hildamar','Sergio','Kinich','Alejandro','Julio','Ivan',
           'Eduardo','Alain','Romina','Pamela','Amaury','Sandra','Little Rock','Tallahassee','Columbus','Wichita')
Agentes[[20,21],1] = random.sample([3,4,5,6,13,14,15,16], k = 2)
print("El zombie", Nombres[20], "llego por la ventana de la casilla x =", Agentes[20,0],", y =", Agentes[20,1])
print("El zombie", Nombres[21], "llego por la ventana de la casilla x =", Agentes[21,0],", y =", Agentes[21,1])

# Agregamos los agentes al mapa
for i in range(22):
    Map[Agentes[i,0],Agentes[i,1]] = Agentes[i,2]

# Aqui junto todo y corre la simulacion
itera = 1
Mapas = np.reshape(Map,(1,20,20))
status = np.array([[itera,2,20,0,0]])
datos = open('Info.txt','w')
datos.write('Iteracion | Zombies | Humanos en la oficina | Humanos salvados | Humanos infectandose \n')
while 1 in Agentes[:,2]:
    Agentes = np.random.permutation(Agentes)
    for i in range (22):
        pos = Agentes [i,[0,1]]
        # Si se esta volviendo zombie
        if Agentes [i,2] in [2,3,4]:
            Agentes [i,2] += 1
        # Si es Zombie
        elif Agentes [i,2] == 5:
            Agentes [i,[0,1]] = ZombieA(pos,i)
        # Si es humano
        elif Agentes [i,2] == 1:
            Agentes [i,[0,1]] = HumanoA(pos,i)
        # Si ya es libre la persona
        elif Agentes [i,2] == 10:
            continue
        # Actualizamos mapa
        Map[pos[0],pos[1]] = 0
        Map[Agentes[i,0],Agentes[i,1]] = Agentes[i,2]
    # Guardar mapa en esta iteración
    Mapas = np.append(Mapas, np.reshape(Map,(1,20,20)), axis = 0)
    # Liberar espacios de personas salvadas
    for i in [15,16,17,18]:
        if Map[i,19] == 10:
            Map[i,19] = 0
            indice = np.where((Agentes[:,0] == i) & (Agentes[:,1] == 19))
            Agentes[indice[0][0],[0,1]] = [0,0]
    # Guardamos vector con iteracion, zombies, personas dentro y salvadas
    z = np.count_nonzero(Agentes[:,2] == 5)
    pd = np.count_nonzero(Agentes[:,2] == 1)
    pf = np.count_nonzero(Agentes[:,2] == 10)
    pi = np.count_nonzero(np.logical_or(Agentes[:,2] == 2, Agentes[:,2] == 3, Agentes[:,2] == 4))
    status = np.append(status,[[itera,z,pd,pf,pi]],axis = 0)
    unido = " ".join([str(itera),'|',str(z),'|',str(pd),'|',str(pf),'|',str(pi),'\n'])
    datos.write(unido)
    # Actualizamos contador
    itera += 1

datos.close()