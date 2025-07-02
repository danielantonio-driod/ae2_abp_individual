# AE2_ABP-Ejercicio individual[Actividad Evaluada]
# 1. Imprime "Hola, mundo"
print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Valeria"
print("Hola,", nombre)                  # con coma
print("Hola " + nombre)                 # con '+'

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 156
print("Hola", numero, "!")              # con coma

# print("Hola " + numero + "!")         # error: no concatena str + int
print("Hola " + str(numero) + "!")      # corregido con str()

# 4. Imprimir “¡Me encanta comer tacos y arepas!” con variables de comida
comida1 = "tacos"
comida2 = "arepas"
print(f"¡Me encanta comer {comida1} y {comida2}!")  #  f-string
print(f"¡Me encanta comer {comida1} y {comida2}!")  #  f-string

# BONUS NINJA: otros métodos de cadena
mensaje = "apREndí Python"
print(mensaje.upper())                 # MAYÚSCULAS
print(mensaje.lower())                 # minúsculas
print(mensaje.capitalize())            # Sólo la primera letra en mayúscula
print("-".join([comida1, comida2]))    # Une con guión: "tacos-arepas"