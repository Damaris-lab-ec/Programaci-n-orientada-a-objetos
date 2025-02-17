#aqui tenemos la clase producto con sus respectivos getter y setters para acceder a los atributo
# luego tenemos la clase inventario que tiene una lista de productos y metodos para añadir, eliminar, actualizar, buscar y mostrar productos
class Producto:
    #Una clase producto debe tener un constructorque debe recibir los atributos
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # 123
        self.nombre = nombre  # Sal en Grano
        self.cantidad = cantidad  # Cantidad en stock
        self.precio = precio  # Precio del producto

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    #la clase inventario tiene un contructor que inicia una lista
    def __init__(self):
        self.productos = []  # Lista para almacenar productos
    #Un metodo para poder añadir procuctos
    def añadir_producto(self, id_producto, nombre, cantidad, precio):
        if any(prod.id_producto == id_producto for prod in self.productos):
            print("Error: ID de producto ya existe.")
            return
        nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        self.productos = [prod for prod in self.productos if prod.id_producto != id_producto]
        print("Producto eliminado correctamente.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.id_producto == id_producto:
                if cantidad is not None:
                    prod.cantidad = cantidad
                if precio is not None:
                    prod.precio = precio
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [prod for prod in self.productos if nombre.lower() in prod.nombre.lower()]
        if encontrados:
            for prod in encontrados:
                print(prod)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for prod in self.productos:
                print(prod)
#menu de inicio de inventario

def menu():
    inventario = Inventario()
    while True:
        print("\nSistema de Gestión de Inventario")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            inventario.añadir_producto(id_producto, nombre, cantidad, precio)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco si no desea cambiar): ")
            precio = input("Nuevo precio (deje en blanco si no desea cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
