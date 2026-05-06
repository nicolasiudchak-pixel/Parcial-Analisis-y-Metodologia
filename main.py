import datetime

class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_nombre(self): return self.__nombre
    def get_precio(self): return self.__precio
    def get_stock(self): return self.__stock

    def set_stock(self, cantidad):
        if self.__stock + cantidad < 0:
            return False
        self.__stock += cantidad
        return True

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Pedido:
    def __init__(self, cliente, productos, total):
        self.cliente = cliente
        self.productos = productos
        self.total = total
        self.fecha = datetime.datetime.now()

class Foodtruck:
    def __init__(self, nombre):
        self.nombre_negocio = nombre
        self.__inventario = []
        self.__historial_ventas = []

    def agregar_producto(self):
        print("\n--- ALTA DE PRODUCTO ---")
        n = input("Nombre: ")
        p = float(input("Precio: "))
        s = int(input("Stock inicial: "))
        self.__inventario.append(Producto(n, p, s))

    def registrar_venta(self):
        print("\n--- NUEVA VENTA (PEDIDO) ---")
        nom_cliente = input("Nombre del Cliente: ")
        tel_cliente = input("Teléfono: ")
        cliente = Cliente(nom_cliente, tel_cliente) # Relación con DER

        prod_nombre = input("Producto a vender: ")
        for p in self.__inventario:
            if p.get_nombre().lower() == prod_nombre.lower():
                cant = int(input(f"Cantidad: "))
                if p.set_stock(-cant):
                    total = p.get_precio() * cant
                    nuevo_pedido = Pedido(cliente, [p.get_nombre()], total)
                    self.__historial_ventas.append(nuevo_pedido)
                    print(f"✓ Pedido registrado para {cliente.nombre}. Total: ${total}")
                else:
                    print("✘ Error: Sin stock suficiente.")
                return
        print("✘ Producto no encontrado.")

    def mostrar_inventario(self):
        print(f"\n--- INVENTARIO {self.nombre_negocio} ---")
        for p in self.__inventario:
            print(f"{p.get_nombre()} - Stock: {p.get_stock()} - ${p.get_precio()}")

    def menu(self):
        while True:
            print(f"\n1. Agregar Producto\n2. Registrar Venta\n3. Ver Inventario\n4. Salir")
            op = input("Seleccione: ")
            if op == "1": self.agregar_producto()
            elif op == "2": self.registrar_venta()
            elif op == "3": self.mostrar_inventario()
            elif op == "4": break

if __name__ == "__main__":
    app = Foodtruck("SmartGastro")
    app.menu()