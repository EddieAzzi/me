TODO: Reflect on what you learned this week and what is still unclear.

.. to navigate backwards in folders
make sure to PUSH screenshots
python ../course/week1/tests.py
F5 to run code on .py
exercise has been pushed
to push: save work, click 'fork' icon, then + to bump it to "staged changes", then 3 dots, "push"
make sure to commit changes with 'tick' icon

import turtle
import random


turtle.shape("turtle")
turtle.color('#%06x' % random.randint(0, 2**24 - 1))
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
print('Eddie')
turtle.forward(10)
turtle.right(90)
turtle.right(90)
turtle.forward(50)