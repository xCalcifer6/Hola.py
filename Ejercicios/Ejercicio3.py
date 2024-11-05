
mi_agenda = dict()
mi_agenda = {
        {"Juan Perez": 35132412},
        {"Tomas Tomasito": 32132132},
        {"Franco Quito": 36465465}
        }
print("AGENDA TELEFÓNICA")
Agenda_Telefonica = input("¿Que accion desea realizar?")
if Agenda_Telefonica == "Agendar":
 
        numero_telefonico = input("Número Telefónico:")
        nombre_completo = input("Nombre")
        mi_agenda.update({"Numero Telefonico":numero_telefonico, "Nombre Completo":nombre_completo})
elif Agenda_Telefonica == "Buscar":
    buscar_numero = input("")

    print(mi_agenda)
        









#mi_agenda = { "Nombre Completo": "",             "Numero Telefonico": ""}


