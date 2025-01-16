print("Bienvenido a tu perfil de usuario")
print("introduce tu nombre ")


nombre_usuario = input().capitalize()
print(nombre_usuario,"Introduce tu sexo")

sexo_usuario = input().lower()
elecciones_validas = ["masculino" , "femenino"]
if sexo_usuario not in elecciones_validas:
    exit()
else: next

print(nombre_usuario, "de que región provienes?")
region_opciones = "Venezuela" , "Estados unidos" , "España"
print(region_opciones)
region_usuario = input().capitalize()
if region_usuario not in region_opciones:
    exit()
else:
    if region_usuario == "Venezuela":
        print("Cuál es tu cosa favorita de Venezuela?")
        cosa_favorita_Venezuela = "arepas","playas","chicha"
        print("Tus opciones son: ", cosa_favorita_Venezuela)
        cosa_favoritaV = input().lower()
        if cosa_favoritaV not in cosa_favorita_Venezuela:
            exit()
        else: next

    if region_usuario == "Estados unidos":
        print("Cuál es tu cosa favorita de Estados unidos?")
        cosa_favorita_Usa = "thanksgiving","hot dog","futbol americano"
        print("Tus opciones son: ", cosa_favorita_Usa)
        cosa_favoritaU = input().lower()
        if cosa_favoritaU not in cosa_favorita_Usa:
            exit()
        else: next

    if region_usuario == "España":
        print("Cuál es tu cosa favorita de España?")
        cosa_favorita_España = "paella","flamenco","real madrid"
        print("tus opciones son: ", cosa_favorita_España)
        cosa_favoritaE = input().lower()
        if cosa_favoritaE not in cosa_favorita_España:
            exit()
        else: next