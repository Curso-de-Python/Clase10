'''
-----------------------------
 EJERCICIO N°1
 Módulo random
-----------------------------
'''
# RANDOM() Y SEED()
from random import random, seed

for i in range(5):
  print(random())

# Probar con seed() y seed(0)

'''
# RANGOS
from random import randrange, randint

print(randrange(5))
print(randrange(0, 5))
print(randrange(0, 5, 2))
print(randint(0, 5))

# ¿NÚMEROS REPETIDOS?
from random import randint

for i in range(10):
  print(randint(1,10), end = ',')

# CHOICE(), SAMPLE()
from random import choice, sample

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lista))
print(sample(lista, 5))
print(sample(lista, 10))
'''
