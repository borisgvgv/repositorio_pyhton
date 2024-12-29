"""
Existe una orden "if" para comprobar condiciones. La condición que se verifica 
no necesita estar indicada entre paréntesis, al contrario que en los lenguajes 
que derivan de C (como C, C++, C#, Java, PHP y algún otro).
La línea del "if" debe terminar con un símbolo de "dos puntos", 
y todo el bloque de órdenes que se va a ejecutar en caso de que se cumpla 
la condición, estará tabulado algo más a la derecha (típicamente 4 espacios; 
el mínimo es dos... o un carácter de tabulación).
Para indicar qué hacer si no se cumple la condición, 
tenemos una cláusula "else" opcional, que también debe ir seguida por un símbolo de "dos puntos":

"""

num1 = int(input("Dime un numero "))
num2 = int(input("Dime otro numero "))
if num1 > num2:
    print("El primero es mayor")
else:
    print("El segundo es mayor")
