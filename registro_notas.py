"""Registro sencillo de estudiantes y notas mediante un diccionario."""

estudiantes = {}

while True:
    print("\n--- REGISTRO DE NOTAS ---")
    print("1. Agregar estudiante")
    print("2. Mostrar todos")
    print("3. Buscar estudiante")
    print("4. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        nombre = input("Nombre del estudiante: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            continue
        try:
            nota = float(input("Nota (0 a 10): "))
        except ValueError:
            print("Ingrese una nota numérica válida.")
            continue
        if not 0 <= nota <= 10:
            print("La nota debe estar entre 0 y 10.")
            continue
        estudiantes[nombre] = nota
        print(f"Se guardó la nota de {nombre}.")

    elif opcion == "2":
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            print("\nESTUDIANTE | NOTA")
            for nombre, nota in estudiantes.items():
                print(f"{nombre} | {nota:g}")

    elif opcion == "3":
        nombre = input("Nombre que desea buscar: ").strip()
        if nombre in estudiantes:
            print(f"{nombre}: {estudiantes[nombre]:g}")
        else:
            print("Estudiante no encontrado.")

    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")
