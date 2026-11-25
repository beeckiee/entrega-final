import dataset

# Conexión con la base de datos
miBase = dataset.connect("sqlite:///base.db")
tabla = miBase["Productos"]

while True:

    opciones = input(
        "\n--- MENÚ DE PRODUCTOS ---\n"
        "A  - Agregar producto\n"
        "L  - Listar productos\n"
        "S  - Salir\n"
        "BT - Buscar en toda la base\n"
        "R  - Remover por nombre\n"
        "ID - Borrar por ID\n"
        "AC - Actualizar producto\n"
        "\nElegí una opción: "
    ).strip().upper()

    match opciones:

        case "A":
            agregarProducto = input("\nProducto: ").strip()

            if not agregarProducto:
                print("El nombre no puede estar vacío.")
                continue

            try:
                agregarPrecio = float(input("Precio: ").strip())

                if agregarPrecio < 0:
                    print("El precio no puede ser negativo.")
                    continue

            except ValueError:
                print("Error: ingresá un precio válido.")
                continue

            agregarCategoria = input("Categoría: ").strip()

            agregar = {
                "Nombre": agregarProducto,
                "Precio": agregarPrecio,
                "Categoria": agregarCategoria
            }

            tabla.insert(agregar)
            print("\n¡Producto agregado con éxito!")

        case "S":
            print("\n¡Hasta la próxima!")
            break

        case "L":
            print("ENTRASTE EN LA OPCION LISTAR")
            
            productos = list(tabla)

            if not productos:
                print("\nLa base de datos está vacía.")
            else:
                for items in productos:
                    print(
                        f'\nID: {items["id"]} | '
                        f'Producto: {items["Nombre"]} | '
                        f'Precio: {items["Precio"]} | '
                        f'Categoría: {items["Categoria"]}'
                    )
                    
                input("\nPresioná ENTER para continuar...")
                    
        case "R":
            removerNombre = input(
                "\nProducto a remover: "
            ).strip()

            eliminados = tabla.delete(Nombre=removerNombre)

            if eliminados:
                print(f"\n{removerNombre} se ha quitado con éxito.")
            else:
                print("\nNo se encontró ese producto.")

        case "ID":
            try:
                borrarID = int(input("\nID del producto a borrar: "))

            except ValueError:
                print("\nIngresá un ID numérico válido.")
                continue

            eliminados = tabla.delete(id=borrarID)

            if eliminados:
                print(f"\nEl producto con ID {borrarID} fue eliminado.")
            else:
                print("\nNo se encontró ese ID.")

        case "AC":
            try:
                idBuscar = int(input("\nID a actualizar: "))

            except ValueError:
                print("\nIngresá un ID válido.")
                continue

            productoExistente = tabla.find_one(id=idBuscar)

            if productoExistente is None:
                print("\nNo existe un producto con ese ID.")
                continue

            nombreActualizar = input("\nNombre nuevo: ").strip()

            try:
                precioActualizar = float(
                    input("Precio nuevo: ").strip()
                )

                if precioActualizar < 0:
                    print("El precio no puede ser negativo.")
                    continue

            except ValueError:
                print("\nIngresá un precio válido.")
                continue

            catActualizar = input("Categoría nueva: ").strip()

            actualizar = {
                "Nombre": nombreActualizar,
                "Precio": precioActualizar,
                "Categoria": catActualizar
            }

            tabla.update(actualizar, ["id"], {"id": idBuscar})

            print("\n¡Producto actualizado con éxito!")

        case "BT":
            buscarTodo = input(
                "\nProducto a buscar: "
            ).strip()

            encontrados = list(tabla.find(Nombre=buscarTodo))

            if encontrados:
                for encontrado in encontrados:
                    print(
                        f'\n{encontrado["Nombre"]} '
                        f'Se encontró en ID: {encontrado["id"]} | '
                        f'Precio: {encontrado["Precio"]} | '
                        f'Categoría: {encontrado["Categoria"]}'
                    )
            else:
                print("\nNo se encontraron productos.")

        case _:
            print("\nOpción inválida. Intentá nuevamente.")