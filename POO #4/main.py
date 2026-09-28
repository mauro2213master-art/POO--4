from inventario import Producto, Inventario


def main():
    inventario = Inventario()

    lapiz = Producto("A1", "Lápiz", 1000, 10)
    cuaderno = Producto("A2", "Cuaderno", 5000, 2)
    inventario.agregar_producto(lapiz)
    inventario.agregar_producto(cuaderno)

    # vender("A1", 3) debe devolver 3000
    total_venta = inventario.vender("A1", 3)
    print(f"vender(A1, 3) = {total_venta} (esperado: 3000)")

    # Vender 5 cuadernos (solo hay 2) debe lanzar error
    try:
        inventario.vender("A2", 5)
        print("ERROR: debió lanzar excepción por stock insuficiente")
    except ValueError as e:
        print(f"OK - stock insuficiente: {e}")

    # Vender un código inexistente debe lanzar error
    try:
        inventario.vender("Z9", 1)
        print("ERROR: debió lanzar excepción por código inexistente")
    except ValueError as e:
        print(f"OK - código inexistente: {e}")

    # Agregar un código repetido debe lanzar error
    try:
        inventario.agregar_producto(Producto("A1", "Lápiz duplicado", 1200, 5))
        print("ERROR: debió lanzar excepción por código duplicado")
    except ValueError as e:
        print(f"OK - código duplicado: {e}")

    # Tras la venta: valor_total() = (1000*7) + (5000*2) = 17000
    valor_total = inventario.valor_total()
    print(f"valor_total() = {valor_total} (esperado: 17000)")

    # productos_con_bajo_stock(5) debe devolver ["Cuaderno"]
    print(f"productos_con_bajo_stock(5) = {inventario.productos_con_bajo_stock(5)} "
          f"(esperado: ['Cuaderno'])")

    # Crear un producto con precio negativo debe lanzar error
    try:
        Producto("B1", "Borrador", -500, 10)
        print("ERROR: debió lanzar excepción por precio negativo")
    except ValueError as e:
        print(f"OK - precio negativo: {e}")


if __name__ == "__main__":
    main()
