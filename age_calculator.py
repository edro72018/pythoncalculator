from datetime import datetime

# Fecha actual
today = datetime.now()

# Diccionario de meses
months = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

# Obtener nombre del mes actual
name_month = months[today.month]

# Pedimos datos
user_input_day = int(input("¿Qué día es tu cumpleaños? "))
user_input_month = int(input("¿Qué mes cumples años?"))
user_input_year = int(input("¿En qué año naciste? "))

# Mostramos info
print(f"Hoy es {today.day} de {name_month}, del año {today.year}")
print(f"Tu cumpleaños es el {user_input_day} de {months[user_input_month]} de {user_input_year}")
