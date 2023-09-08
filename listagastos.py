import sqlite3
import os

# Inicializar la base de datos
def init_database():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        description TEXT,
        amount REAL
    )
    """)

    conn.commit()
    conn.close()

# Registrar un gasto
def add_expense(date, description, amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO expenses (date, description, amount) VALUES (?, ?, ?)", (date, description, amount))

    conn.commit()
    conn.close()

# Listar todos los gastos
def list_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    if expenses:
        print("Listado de Gastos:")
        for expense in expenses:
            print(f"{expense[0]}. Fecha: {expense[1]}, Descripción: {expense[2]}, Monto: ${expense[3]}")
    else:
        print("No hay gastos registrados.")

    conn.close()

# Función principal
def main():
    init_database()

    while True:
        print("\n1. Registrar gasto")
        print("2. Listar gastos")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            date = input("Ingrese la fecha (YYYY-MM-DD): ")
            description = input("Ingrese la descripción: ")
            amount = float(input("Ingrese el monto: $"))
            add_expense(date, description, amount)
            print("Gasto registrado con éxito.")
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()

