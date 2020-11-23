'''
-----------------------------
 EJERCICIO
 Creando tu primer módulo
-----------------------------
 Este código no es para ejecutarse, aquí encontrarás instrucciones que puedes copiar y pegar en un nuevo Repl para la creación de un módulo
-----------------------------
'''
# En main.py
import modulo
print(modulo.contador)

# En modulo.py
print("¡Ser un módulo es genial!")
print(__name__)

contador = 0

if __name__ == "__main__":
  print("Llamado desde el mismo modulo.py")
else:
  print("Llamado desde main.py")

# -----------------------------
# EN MODULO.PY - FINAL

#!/usr/bin/env python3
"""modulo.py - Ejemplo de módulo"""

__contador = 0

def suma(lista):
  global __contador
  __contador += 1
  suma = 0
  for elem in lista:
    suma += elem
  return suma

def producto(lista):
  global __contador
  __contador += 1
  producto = 1
  for elem in lista:
    producto *= elem
  return producto

if __name__ == "__main__":
  print("Llamado desde el modulo")
  l = [i+1 for i in range(5)]
  print(suma(l) == 15)
  print(producto(l) == 20)

# EN MAIN.PY - FINAL

from modulo import suma, producto

ceros = [0 for i in range (5)]
unos = [1 for i in range (5)]
print(suma(ceros))
print(producto(unos))

# -----------------------------
# Prueba de path

from sys import path
for i in path: print(i)

# -----------------------------
# Importar desde otra carpeta
from sys import path
path.append('C:\\Users\\adria\\OneDrive\\Documentos\\Engitronic-DESKTOP-TLCG3SD\\Curso de Python\\Jupyter\\modulos')

import modulo
ceros = [0 for i in range (5)]
unos = [1 for i in range (5)]
print(modulo.suma(ceros))
print(modulo.producto(unos))

# -----------------------------
# Tu primer paquete

from sys import path
path.append('C:\\Users\\adria\\OneDrive\\Documentos\\Engitronic-DESKTOP-TLCG3SD\\Curso de Python\\Clases\\Clase 10\\paquetes')

import extra.iota

print(extra.iota.FunI())
