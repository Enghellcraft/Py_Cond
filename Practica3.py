candidato = input(f"Ingrese un candidato: ")
candidato_minus = candidato.lower()
if (candidato_minus== "a"):
    print(f"Ud ha votado por el Partido Rojo")
elif (candidato_minus== "b") :
    print(f"Ud ha votado por el Partido Verde")
elif (candidato_minus=="c") :
    print(f"Ud ha votado por el Partido Azul")
else :
    print(f"No existe tal Candidato")