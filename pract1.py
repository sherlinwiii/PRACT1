class Pila:
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.pila = []
    
    def insertar(self, elemento):
        if len(self.pila) < self.capacidad:
            self.pila.append(elemento)
            print(f"Insertado: {elemento}")
        else:
            print("Error: La pila está llena.")
    
    def eliminar(self):
        if self.pila:
            eliminado = self.pila.pop()
            print(f"Eliminado: {eliminado}")
        else:
            print("Error: La pila está vacía.")
    
    def mostrar(self):
        print("Estado actual de la pila:")
        for elemento in reversed(self.pila):
            print(f"[{elemento}]")
        print("----" if self.pila else "[Vacía]")

pila = Pila()

def menu():
    while True:
        print("\nOperaciones disponibles:")
        print("1. Insertar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar pila")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            elem = input("Ingrese el elemento a insertar: ")
            pila.insertar(elem)
        elif opcion == "2":
            pila.eliminar()
        elif opcion == "3":
            pila.mostrar()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu()
