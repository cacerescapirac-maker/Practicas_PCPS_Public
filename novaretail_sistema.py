"""
Sistema de gestión de ventas para Nova Retail.
"""
def validar_stock(stock_actual: int, cantidad: int) -> bool:
    """
    Verifica si existe stock suficiente.
    """
    return stock_actual >= cantidad
def calcular_total(
    precio_unitario: float,
    cantidad: int,
    igv_porcentaje: float
) -> tuple[float, float, float]:
    """
    Calcula subtotal, IGV y total de la venta.
    """
    subtotal = precio_unitario * cantidad
    igv = subtotal * igv_porcentaje
    total = subtotal + igv

    return subtotal, igv, total
def procesar_venta(
    codigo_producto: str,
    cantidad: int,
    stock_actual: int,
    precio_unitario: float,
    igv_porcentaje: float
) -> tuple[float, int] | None:
    """
    Procesa una venta y actualiza el stock.
    """
    if not validar_stock(stock_actual, cantidad):
        print("Sin stock suficiente")
        return None

    _, _, total = calcular_total(
        precio_unitario,
        cantidad,
        igv_porcentaje
    )
    nuevo_stock = stock_actual - cantidad
    print(f"Venta registrada: {codigo_producto} {total}")
    return total, nuevo_stock
