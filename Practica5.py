anio = int(input(f"Ingrese un anio: "))
if (((anio%4==0)and(anio%100!=0))or((anio%4==0)and(anio%100!=0)and(anio%400==0))) :
    print(f"Es bisiesto :)")
else :
    print(f"No es bisiesto :(")