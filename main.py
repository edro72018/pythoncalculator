import age_calculate

#Main function to test the age calculator
if __name__ == "__main__":
        print("Bienvenido al Calculadora")
        print("Elige una opción:\n")
        print("1. Calcular edad")
        print("2. Cronómetro (Próximamente)")
        print("3. Temporizador (Próximamente)")
        print("4. Operaciones matemáticas (Próximamente)")
        print("0. Salir")
        while True:
            try:
                option = int(input("Selecciona una opción: "))
            except ValueError:
                print("Por favor, ingresa un número válido.\n")
                continue
            except KeyboardInterrupt:
                print(f"\nSaliendo. Baiii¡")
                exit()

            if option == 0:
                print("Ok, Baiii!")
                exit()
            elif option == 1:
                birthday = age_calculate.ask_birthday()
                age_calculate.calculate_age(birthday)
            elif option in [2, 3, 4]:
                print("Funcionalidad en desarrollo. Por favor, elige otra opción.\n")
                continue
            else:
                continue


