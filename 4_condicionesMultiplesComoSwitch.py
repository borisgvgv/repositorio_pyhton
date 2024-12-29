"""
 No existe "switch" o "case", pero se pueden enlazar varios "if" sin necesidad de tabular cada vez más a la derecha, si se emplea "elif" (abreviatura de "else if"):
"""

nota = int(input("Introduzca la nota "))
if nota == 5:
    print("Sobresaliente alto")
elif nota == 4:
    print("Nota media")
elif nota == 3:
    print("Nota baja")
elif nota < 2:
        print("Suspenso")
