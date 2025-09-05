from datetime import datetime
"""
declaración de variables
"""# Fecha actual
TODAY = datetime.now()

# Diccionario
MONTHS = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

# Obtener nombre del mes actual
name_month = MONTHS[TODAY.month]

maximum_age = 120

#Pedimos datos
#Primer while es para el programa en general
while True:
    try:
        # Validar fecha completa con datetime
        while True:
            try:
                user_input_day = int(input("¿Qué día es tu cumpleaños? "))
                while True:
                    user_input_month = int(input("¿Qué mes cumples años? "))
                    if user_input_month in MONTHS:
                        break
                    else:
                        print("Mes inválido (1 - 12)")
                user_input_year = int(input("¿En qué año naciste? "))

                # Construir la fecha
                birthday = datetime(user_input_year, user_input_month, user_input_day)

                # Validar que la edad no supere el máximo
                if TODAY.year - user_input_year > maximum_age:
                    print(f"Por favor, ingresa un año de nacimiento válido (máx {maximum_age} años). ")
                    continue
                
                if TODAY.year < user_input_year:
                    print(f"Ingresa un año válido, máximo {TODAY.year}. ")
                    continue

                break  
            # Fecha válida → salimos del bucle

            except ValueError:
                print(f"Fecha inválida. ¿Tu fecha de nacimiento es el {user_input_day} de {MONTHS[user_input_month]} de {user_input_year}?   \n")

        #Menciona el día que es hoy
        print(f"\nHoy es {TODAY.day} de {name_month} del {TODAY.year}")
        #Menciona el día de cumpleaños
        print(f"Tu cumpleaños es el {user_input_day} de {MONTHS[user_input_month]}. ")
        if TODAY.month > user_input_month or (TODAY.month == user_input_month and TODAY.day > user_input_day):
            print(f"Tienes {TODAY.year - user_input_year} años.\n")
        elif TODAY.month == user_input_month and TODAY.day == user_input_day:
            print("¡Feliz cumpleaños!")
            print(f"Cumples {TODAY.year - user_input_year} años.\n")
        else: 
            print(f"Tienes {TODAY.year - user_input_year - 1} años.\n")
            
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
        print(f"{ValueError} es un dato inválido. \nPor favor, ingresa valores válidos.\n")
    except NameError:
       print(f"Es un dato inválido. \nPor favor, ingresa valores válidos.\n")
    except KeyboardInterrupt:
        print("¡Hasta luego!\n")
        exit()