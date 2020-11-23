'''
-----------------------------
 EJERCICIO N°2
 Caracteres y cadenas
-----------------------------
'''
# CADENAS MULTILÍNEA
multiLinea = '''Linea #1
Linea #2'''
print(len(multiLinea))

'''
# ---------------------------
# PUNTO DE CÓDIGO
ch1 = 'a' 
ch2 = ' ' # espacio

print(ord(ch1))
print(ord(ch2))

print(chr(97))
print(chr(945))

# ---------------------------
# CADENAS COMO SECUENCIAS
ejemploString = 'silly walks'

# Indexación
for i in range(len(ejemploString)):
  print(ejemploString[i], end=' ')

print()

# Iteraciones
for ch in ejemploString:
  print(ch, end=' ')

print()

# ---------------------------
# RODAJAS
alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[3:-2])
print(alpha[::2])   # inicio:fin:paso

# ---------------------------
# IN Y NOT IN 
alfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" in alfabeto)
print("1" in alfabeto)
print("Xyz" not in alfabeto)

# ---------------------------
# INSTRUCCIONES PROHIBIDAS
#del alfabeto[0]
#alfabeto.append("A")
#alfabeto.insert(0, "A")

# ---------------------------
# MÍNIMO Y MÁXIMO CARACTER SEGÚN ASCII
print(min("aAbByYzZ"))
print(max("aAbByYzZ"))

t = '¡Tic Tac Toe!'
print('[' + min(t) + ']')
print('[' + max(t) + ']')

# ---------------------------
# POSICIÓN DEL CARACTER ESPECIFICADO
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))

# ---------------------------
# CONVERSIÓN A LISTA
print(list("abcabc"))

# ---------------------------
# CONTEO DE REPETICIONES
print("abcabc".count("b"))
print('abcabc'.count("d"))

# ---------------------------
# MÉTODO .CAPITALIZE()
print('aBcD'.capitalize())

# ---------------------------
# MÉTODO .CENTER()
print('['+'alfa'.center(10)+']')
print('['+'gamma'.center(20, '*')+']')

# ---------------------------
# MÉTODO .ENDSWITH()
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("eta"))

# ---------------------------
# MÉTODO .FIND()
print("beta".find("ta"))
print("beta".find("mma"))
#print('kappa'.find('a', 2))
#print('kappa'.find('a', 2, 4))

# ---------------------------
# MÉTODO .ISALNUM()
print('lambda30'.isalnum())
print('@'.isalnum())
print('lambda 30'.isalnum())

# ---------------------------
# MÉTODOS .ISALPHA() Y .ISDIGIT()
print('lambda'.isalpha())
print("Año2019".isdigit())

# ---------------------------
# MÉTODO .JOIN()
print(",".join(["omicron", "pi", "rho"]))

# ---------------------------
# MÉTODO .LOWER()
print("SiGmA=60".lower())

# ---------------------------
# MÉTODO .LSTRIP()
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

# ---------------------------
# MÉTODO .REPLACE()
print("www.netacad.com".replace("netacad", "pythoninstitute"))
print("Apple juice".replace("juice", ""))
print("This is it!".replace("is", "are", 1)) 

# ---------------------------
# MÉTODO .SPLIT()
print("phi       chi\npsi".split())

# ---------------------------
# MÉTODO .SWAPCASE()
print("Yo sé que nada sé.".swapcase())

# ---------------------------
# MÉTODO .TITLE()
print("Yo sé que nada sé. Parte 1.".title())

# ---------------------------
# MÉTODO .UPPER()
print("Yo sé que nada sé. Parte 2.".upper())

# ---------------------------
# COMPARACIÓN DE CADENAS
'alfa' == 'alfa'
'alfa' != 'Alfa'

'alfa' < 'alfabeto'
'beta' > 'Beta'

'10' == '010'
'10' > '010'
'10' == 10
#'10' > 10   # Error

# ---------------------------
# ORDENAMIENTO DE CADENAS
# Función sorted()
griego1 = ['omega', 'alfa', 'pi', 'gama']
griego2 = sorted(griego1)

print(griego1)
print(griego2)

# Método sort()
griego1 = ['omega', 'alfa', 'pi', 'gama']
griego1.sort()
print(griego1)
print(2**0.5)
print(pow(2,0.5))
'''
