from datetime import datetime
"""
declaración de variables y constantes
"""
TODAY = datetime.now()
# Diccionario
MONTHS = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}
MINIMUM_YEAR = datetime.now().year - 120

#Función para pedir datos
def ask_birthday() -> datetime:
    """Pide y valida la fecha de cumpleaños del usuario."""
    today = datetime.now()

    while True:
        try:
            user_day = int(input("¿Qué día es tu cumpleaños? "))
            while True:
                user_month = int(input("¿Qué mes cumples años? "))
                if user_month not in MONTHS:
                    print("Mes inválido (1 - 12).")
                    continue
                break
            while True:
                user_year = int(input("¿En qué año naciste? "))

                #Validar rango de años
                if user_year < MINIMUM_YEAR:
                    print(f"En serio naciste en el {user_year}?. No te lo creo.")
                    continue
                if user_year > today.year:
                    print(f"No puedes haber nacido en el {user_year}. ¿Vienes del futuro?")
                    continue
                break

            # Construir fecha valida, días correctos y años bisiestos
            birthday = datetime(user_year, user_month, user_day)

            return birthday

        except ValueError:
            print("Data inválida. Intenta de nuevo.\n")
        except NameError:
            print(f"Es un dato inválido. \nPor favor, ingresa valores válidos.\n")
        except KeyboardInterrupt:
                print(f"\nSaliendo. Baiii¡")
                exit()

def calculate_age(birthday: datetime) -> int:
    name_month = MONTHS[TODAY.month]
    #Menciona el día que es hoy
    print(f"\nHoy es {TODAY.day} de {name_month} del {TODAY.year}")
    #Menciona el día de cumpleaños
    print(f"Tu cumpleaños es el {birthday.day} de {MONTHS[birthday.month]}")
    if TODAY.month > birthday.month or (TODAY.month == birthday.month and TODAY.day > birthday.day):
        print(f"Tienes {TODAY.year - birthday.year} años.\n")
    elif TODAY.month == birthday.month and TODAY.day == birthday.day:
        print("¡Feliz cumpleaños!")
        print(f"Cumples {TODAY.year - birthday.year} años.\n")
    else: 
        print(f"Tienes {TODAY.year - birthday.year - 1} años.\n")