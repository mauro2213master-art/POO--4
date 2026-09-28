"""
Clases Producto e Inventario.

Encapsulamiento: los atributos se guardan con prefijo `_` (privados por
convención en Python) y se exponen solo mediante properties (getters).
El stock nunca se modifica directamente desde fuera: la única vía es
Producto.aumentar_stock() / Producto.disminuir_stock(), y a su vez
Inventario.vender() es la única vía pública para descontar stock desde
el inventario.
"""


class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    # ---------- Getters (properties de solo lectura) ----------

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def precio(self) -> float:
        return self._precio

    @property
    def stock(self) -> int:
        return self._stock

    # ---------- Manejo de stock ----------

    def aumentar_stock(self, n: int) -> None:
        if n <= 0:
            raise ValueError("n debe ser mayor que 0")
        self._stock += n

    def disminuir_stock(self, n: int) -> None:
        if n <= 0:
            raise ValueError("n debe ser mayor que 0")
        if n > self._stock:
            raise ValueError(
                f"No se puede disminuir {n} unidades: solo hay {self._stock} en stock"
            )
        self._stock -= n

    def __repr__(self) -> str:
        return (f"Producto(codigo={self._codigo!r}, nombre={self._nombre!r}, "
                f"precio={self._precio}, stock={self._stock})")


class Inventario:
    def __init__(self):
        self._productos: dict[str, Producto] = {}
        self._historial_ventas: list[dict] = []

    def agregar_producto(self, producto: Producto) -> None:
        if producto.codigo in self._productos:
            raise ValueError(f"Ya existe un producto con el código: {producto.codigo}")
        self._productos[producto.codigo] = producto

    def vender(self, codigo: str, cantidad: int) -> float:
        producto = self._productos.get(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código: {codigo}")
        if cantidad > producto.stock:
            raise ValueError(
                f"Stock insuficiente para '{producto.nombre}': "
                f"hay {producto.stock}, se pidieron {cantidad}"
            )

        producto.disminuir_stock(cantidad)  # única vía de cambio de stock
        total = producto.precio * cantidad
        self._historial_ventas.append(
            {"codigo": codigo, "cantidad": cantidad, "total": total}
        )
        return total

    def valor_total(self) -> float:
        return sum(p.precio * p.stock for p in self._productos.values())

    def productos_con_bajo_stock(self, limite: int) -> list[str]:
        return [p.nombre for p in self._productos.values() if p.stock < limite]

    def total_ventas_registradas(self) -> int:
        """Cantidad de ventas registradas hasta ahora (útil para pruebas)."""
        return len(self._historial_ventas)
