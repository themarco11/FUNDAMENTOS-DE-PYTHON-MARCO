class CalculadorA:
    # Calculadora básica en Python

    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        if b == 0:
            return "Error: No se puede dividir entre cero."
        return a / b

    def potencia(a, b):
        return a ** b

class main():
    print("=== Calculadora Básica ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Salir")

    while True:
        opcion = input("\nElige una opción (1-6): ")

        if opcion == "6":
            print("¡Hasta luego!")
            break

        if opcion not in ["1", "2", "3", "4", "5"]:
            print("Opción no válida. Intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos.")
            continue

        if opcion == "1":
            print(f"Resultado: {CalculadorA.sumar(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {CalculadorA.restar(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {CalculadorA.multiplicar(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {CalculadorA.dividir(num1, num2)}")
        elif opcion == "5":
            print(f"Resultado: {CalculadorA.potencia(num1, num2)}")

# Ejecutar la calculadora
if __name__ == "__main__":
    main()
