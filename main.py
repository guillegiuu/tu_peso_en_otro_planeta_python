# Python Control Flow CodeCademy
# Informacion de los Planetas
print("Tengo información para los siguientes planetas:\n")

print("   1. Venus    2. Marte    3. Jupiter")
print("   4. Saturno  5. Urano   6. Neptuno")

# Peso
peso = 185

# Planeta
planeta = 3

# Utilizo if para comprobar y ademas comprobar el peso de codey en Jupiter:

# If
if planeta == 3:
  print("Jupiter")

# Imprimo por pantalla el peso en Jupiter de Codey.
print(peso * 2.34)

# =========================================================

# Informacion de los Planetas
print("Tengo información para los siguientes planetas:\n")

print("   1. Venus    2. Marte    3. Jupiter")
print("   4. Saturno  5. Urano   6. Neptuno")

# Peso
peso = 185

# Planeta
planeta = 3

# Sentencias if/elif
if planeta == 1:
  peso = peso * 0.91
elif planeta == 2:
  peso = peso * 0.38
elif planeta == 3:
  peso = peso * 2.34
elif planeta == 4:
  peso = peso * 1.06
elif planeta == 5:
  peso = peso * 0.92
elif planeta == 6:
  peso = peso * 1.19

print("Tu peso en otro planeta es:", peso)
"""
========================================================

*
Si quieres modificar el planeta o el peso, solamente modifica \
, los valores de las variables (peso y planeta), ademas \
de modificar el valor str del print del if.

Te dejo una tabla con los valores respectivos de cada planeta:

Venus =	0.91
Marte	= 0.38
Jupiter	= 2.34
Saturno	= 1.06
Urano	= 0.92
Neptuno	= 1.19

"""
