import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        return [producto for producto in self.productos.values() if producto.nombre == nombre]

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: producto.__dict__ for id, producto in self.productos.items()}, f)

    def cargar_inventario(self, archivo):
        with open(archivo, 'r') as f:
            productos = json.load(f)
            self.productos = {id: Producto(**datos) for id, datos in productos.items()}

def menu():
    inventario = Inventario()
    while True:
        print("\n1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Guardar Inventario")
        print("7. Cargar Inventario")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(Producto(id, nombre, cantidad, precio))
        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_por_nombre(nombre)
            for producto in productos:
                print(producto)
        elif opcion == "5":
            inventario.mostrar_todos()
        elif opcion == "6":
            archivo = input("Nombre del archivo para guardar: ")
            inventario.guardar_inventario(archivo)
        elif opcion == "7":
            archivo = input("Nombre del archivo para cargar: ")
            inventario.cargar_inventario(archivo)
        elif opcion == "8":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()