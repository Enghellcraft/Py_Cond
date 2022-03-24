dia = input(f"Ingrese un dia de semana: ")
diaminus = dia.lower()
if (diaminus== "lunes"):
    print(f"Garfield te odiaria!")
elif (diaminus== "viernes") :
    print(f"I'm in love!")
elif ((diaminus=="sabado") or (diaminus=="domingo")) :
    print(f"Finally, some peace and quiet!")
else :
    print(f"Go work!")