dia = input(f"Ingrese un dia de semana: ")
dia_minus = dia.lower()
if (dia_minus == ("lunes" or "martes" or "miercoles")) :
    print(f"Es dia de Examen")
    aprobados = int(input(f"Ingrese los Aprobados "))
    desaprobados = int(input(f"Ingrese los Desaprobados: "))
    print(f"Los Aprobados son: {(aprobados/(aprobados + desaprobados))*100}")
    print(f"Los Desaprobados son: {(desaprobados/(aprobados + desaprobados))*100}")
elif (dia_minus == ("jueves")) :
    asistencias = int(input(f"Ingrese el porcentaje de asistencia: "))
    if (asistencias >= 50) :
        print(f"Asistio la mayoria")
    else :
        print(f"No asistio la mayoria")
elif (dia_minus == ("viernes")) :
    print(f"Clase de Consulta")
    cantidad_alumnos = int(input(f"Ingrese los Alumnos que asisten: "))
    abonos = int(input(f"Ingrese el Abono por Alumno: "))
    print(f"El total abonado es de: {abonos* cantidad_alumnos}")
else :
    print(f"Ese dia no esta en el cronograma")