# Examen-Atomic-Labs
En este repositorio se encuantra la solución al examen de programacion para Atomic Labs, se incluyen dos archivos, es el mismo programa solo que subido como un .ipynb y otro como .py 
- Lo primero que hice fue hacer un array que simulara el mapa donde las personas y zombies se moverian y "Poner las paredes" dando el valor de -1 a los luagres donde esta una pared
- Despues un array de 22x4 donde se pone la posicion de tanto las personas como los zombies, esto porque como las personas se podian volver zombies me resulto mas facil tener a todos junto en un solo array, donde las primeras 2 columas son la posicion en x y y el tercero dice si es persona (1), Zombie (5), si se esta volviendo Zombie (2-4) o si ya esta libre (10), tambien puse un cuarto indice el cual sirve como link a el nombre de la persona o el zombie que esta guardado en otra lista (Durante la semana habia investigado a la empresa y en Linked In encontre una lista con los contactos de varios empleados por lo que decidi agregar el nombre de estos en la simulacion)
- Luego acomode a todos en el mapa, poniendo el valor de su categoria (1-5) en la ubicacion que les correspondia
- Ya con todo esto esta listo para entrar a un while que sigue hasta que no queden personas dentro del mapa, lo primero que hace es hacer aleatorio el orden con el que los agentes se moveran, despues uno por uno checa a que categoria pertenece y dependiendo de cual sea es como actua
  - Si es Zombie corre una funcion en la cual el zombie se movera aleatoriamiente 4 veces un paso a la vez, con la restriccion de que no puede moverse a un lugar que este ocupado o por el que ya haya pasado en ese turno, ademas de esto si en alguno de estos movimientos pasa junto a una persona esta se infectara y su categoria pasara a ser 2
  - Si es persona corre una funcion en la cual la persona se movera 2 veces un paso a la vez, con las mismas restricciones que el zombie pero ademas de esto como el movimiento de los humanos debe ir encaminado hacia la entrada, la probabilidad de moverse entre las casillas disponibles es diferente 
