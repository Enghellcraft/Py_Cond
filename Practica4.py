letra = input(f"Ingrese una Letra: ")
letra_minus = letra.lower()
if (len(letra_minus) == 1):
    if (letra_minus== "a" or letra_minus== "e" or letra_minus== "i" or letra_minus== "o" or letra_minus== "u"):
        print(f"Es una Vocal!")
    else :
        print(f"No es Vocal!")
else:
    print(f"Ud no ingreso una letra sino varias")