# Examen-Atomic-Labs
En este repositorio se encuantra la solución al examen de programacion para Atomic Labs, se incluyen dos archivos, es el mismo programa solo que subido como un .ipynb y otro como .py 
- Lo primero que hice fue hacer un array que simulara el mapa donde las personas y zombies se moverian y "Poner las paredes" dando el valor de -1 a los luagres donde esta una pared
- Despues un array de 22x4 donde se pone la posicion de tanto las personas como los zombies, esto porque como las personas se podian volver zombies me resulto mas facil tener a todos junto en un solo array, donde las primeras 2 columas son la posicion en x y y el tercero dice si es persona (1), Zombie (5), si se esta volviendo Zombie (2-4) o si ya esta libre (10), tambien puse un cuarto indice el cual sirve como link a el nombre de la persona o el zombie que esta guardado en otra lista (Durante la semana habia investigado a la empresa y en Linked In encontre una lista con los contactos de varios empleados por lo que decidi agregar el nombre de estos en la simulacion)
- Luego acomode a todos en el mapa, poniendo el valor de su categoria (1-5) en la ubicacion que les correspondia
- Ya con todo esto esta listo para entrar a un while que sigue hasta que no queden personas dentro del mapa, lo primero que hace es hacer aleatorio el orden con el que los agentes se moveran, despues uno por uno checa a que categoria pertenece y dependiendo de cual sea es como actua
  - Si es Zombie corre una funcion en la cual el zombie se movera aleatoriamiente 4 veces un paso a la vez, con la restriccion de que no puede moverse a un lugar que este ocupado o por el que ya haya pasado en ese turno, ademas de esto si en alguno de estos movimientos pasa junto a una persona esta se infectara y su categoria pasara a ser 2
  - Si es persona corre una funcion en la cual la persona se movera 2 veces un paso a la vez, con las mismas restricciones que el zombie pero ademas de esto como el movimiento de los humanos debe ir encaminado hacia la salida por lo que dividi el mapa en 5 zonas, 3 en la zona superior a la entrada que se ve a la mitad del mapa y 2 en la parte de abajo de esta, esto con el objetivo de que en cada zona la probabilidad de moverse en cierta direccion sea mayor a las otras de manera a que eventualmente el humano tienda a seguir un camino hacia la salida, por ejemplo en la parte inferior del mapa los humanos estan mas encamiados en moverse hacia la derecha que hacia la izquierda o hacia arriba o abajo, mientras que en la parte superior izquierda el humano tiende a moverse hacia la derecha y abajo para poder crurzar por el estrecho que se encuentra en la mitad del mapa. Despues de moverse checa si llega a la salida para cambiar su categoria a 10 o si paso junto a un zombie y se infecta para cambiar su categoria a 2
  - Si esta infectado entonces pasa un turno no se mueve y el contador pasa a 3, esto se repite hasta que llega a 5 y en el proximo turno ya sera un zombie
  - Si ya salio entonces no hace nada
- Despues de que ya pasaron todos los agentes libera los lugares que fueron ocupados en la salida y agrega a un archivo .txt el estado de la simulacion (Núm. iteración | Núm. zombies | Núm. humanos en la oficina | Núm. de humanos salvados). 
