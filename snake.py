"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector
import random #Importar libreria random para elegir colores randomizados despues

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colors = ['green','Yellow','purple', 'pink', 'blue'] #Vector con los colores posibles
c1 = 'red'
c2 = 'red' #Se le asigno un mismo color a las dos variables. 
while c1 == c2: #mientras ambas variales sean iguales, se le asiganrá un color random a cada uno tal que queden distintos. 
    c1 = random.choice(colors)
    c2 = random.choice(colors)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, c1)

    square(food.x, food.y, 9, c2)
    update()
    ontimer(move, 100)

    if head != food: #Establecer la condición de que la vibora aun no se come la comida
        if inside(food) == True:    #Establecer la condición de que la comida este dentro de los limites
            vc = [-10,0,10]  #Vector para determinar los 3 valores posibles de "x" y de "y"
            rd1 = random.choice(vc) #Elegir un elemento random del vector
            rd2 = random.choice(vc) #Elegir un elemento random del vector
            food.x = food.x + rd1 #Asignar una posicion random en x de la comida
            food.y = food.y + rd2  #Asignar una posicion random en y de la comida

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
