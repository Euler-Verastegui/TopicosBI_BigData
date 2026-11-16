print("Estructuras Condicionales")

# Condicional simple
notaTBI = 17
if notaTBI >= 10.51:
    print("Aprobaste")

# Condicional doble
    edad = 17
    if edad >= 18:
        print("Tomar bebidas en exceso es dañino")
    else:
        print("No apto para menores")

# Condicional Anidado
nota = 20
if nota >= 17 & nota<=20:
    print("Alumno Brillante")
elif nota>=14 & nota<17:
    print("Alumno Excelente")
elif nota>13 & nota<15:
    print("Alumno Bueno")
elif nota>10.5 & nota<13:
    print("Alumno Regular")
else:
    print("Alumno con bajo rendimiento")

# Condional Multiple 
""""
Python 3.9.0 a versiones anteriores no existe condicional mmultiple
Todo se trabajaba con IF-ELIF-ELIF-ELSE

Python 3.10 o superior
Se trabaja con MATCH
"""
num = 4
match num:
    case 1: print("Vocal A")
        case 2: print("Vocal A")
        case 3: print("Vocal A") 
        case 4: print("Vocal A")
        case 5: print("Vocal A")
        case _: print("Númeroo no corresponde a vocal")

