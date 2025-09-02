from datetime import datetime
""" Agregar la función para hacer un tipo login, ingrese contraseña o usuario y sin eso que no pueda ejecutar el programa """
# Fecha actual
today = datetime.now()

# Diccionario
months = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

# Obtener nombre del mes actual
name_month = months[today.month]

maximum_age = 120


# Pedimos datos
#Primer while es para el programa en general
while True:
    try:
        """#Es para validar los datos que introduce el usuario
        while True:
            user_input_day = int(input("¿Qué día es tu cumpleaños? "))
            if user_input_day < 1 or user_input_day > 31:
                print("Por favor, ingresa un día válido.")
                continue
            else:
                break
        while True:
            user_input_month = int(input("¿Qué mes cumples años? "))
            if user_input_month < 1 or user_input_month > 12:
                print("Por favor, ingresa un mes válido. (1 - 12)")
                continue
            else:
                break
        while True:
            user_input_year = int(input("¿En qué año naciste? "))
            if today.year - user_input_year > maximum_age:
                print(f"Por favor, ingresa un año de nacimiento válido.")
                continue
            else:
                break
        """

        # Validar fecha completa con datetime
        while True:
            try:
                user_input_day = int(input("¿Qué día es tu cumpleaños? "))
                while True:
                    user_input_month = int(input("¿Qué mes cumples años? "))
                    if user_input_month in months:
                        break
                    else:
                        print("Mes inválido (1 - 12)")
                user_input_year = int(input("¿En qué año naciste? "))

                # Construir la fecha
                #birthday = datetime(user_input_year, user_input_month, user_input_day)

                # Validar que la edad no supere el máximo
                if today.year - user_input_year > maximum_age:
                    print(f"Por favor, ingresa un año de nacimiento válido (máx {maximum_age} años). ")
                    continue
                
                if today.year < user_input_year:
                    print(f"Ingresa un año válido, máximo {today.year}. ")
                    continue

                break  
            # Fecha válida → salimos del bucle

            except ValueError:
                print(f"Fecha inválida. ¿Tu cumpleaños es el {user_input_day} de {months[user_input_month]} de {user_input_year}?   \n")

        #Menciona el día que es hoy
        print(f"\nHoy es {today.day} de {name_month} del {today.year}")
        #Menciona el día de cumpleaños
        print(f"Tu cumpleaños es el {user_input_day} de {months[user_input_month]} de {user_input_year}")
        if today.month > user_input_month or (today.month == user_input_month and today.day > user_input_day):
            print(f"Tienes {today.year - user_input_year} años.\n")
        elif today.month == user_input_month and today.day == user_input_day:
            print("¡Feliz cumpleaños!")
        else: 
            print(f"Tienes {today.year - user_input_year - 1} años.\n")
            
        #Salir del programa (s/n)
        while True:
            quieres_salir = input("¿Quieres salir? (s/n): ")
            if quieres_salir.lower() == "s":
                print("Ok, Baiii!")
                exit()
            elif quieres_salir.lower() == "n":
                break
            else:
                print("Opción no válida.")
                continue
    except ValueError:
        print("Por favor, ingresa valores válidos.")
    except NameError:
        print("Por favor, completa todos los campos.")
    except KeyboardInterrupt:
        print("\n¡Hasta luego!")
        exit()