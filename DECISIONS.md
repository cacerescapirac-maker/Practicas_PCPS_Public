# Decisión de Diseño: División de la función `procesar_venta`

## Contexto

Inicialmente se recibió una única función llamada `procesar_venta()` que concentraba varias responsabilidades:

- Validar disponibilidad de stock.
- Calcular subtotal, IGV y total.
- Actualizar el stock.
- Registrar el resultado de la venta.

Esta implementación funcionaba correctamente, pero presentaba un bajo nivel de modularidad y dificultaba el mantenimiento y las pruebas unitarias.

## Decisión

Se dividió la lógica en tres funciones independientes.

### 1. validar_stock()

**Responsabilidad:** verificar si existe stock suficiente para completar la venta.

### 2. calcular_total()

**Responsabilidad:** realizar exclusivamente los cálculos económicos de la venta.

### 3. procesar_venta()

**Responsabilidad:** coordinar el flujo completo de la venta.

## Criterio arquitectónico utilizado

Se aplicó el Principio de Responsabilidad Única (SRP).

Cada función tiene una única razón para cambiar:

- `validar_stock()`: validación de inventario.
- `calcular_total()`: cálculos monetarios.
- `procesar_venta()`: coordinación del proceso.

## Beneficios obtenidos

- Mayor modularidad.
- Mayor legibilidad.
- Menor acoplamiento.
- Facilidad para pruebas unitarias.
- Mayor mantenibilidad.

## Resultado

La función original fue refactorizada en componentes con responsabilidades específicas, aplicando el Principio de Responsabilidad Única (SRP) y mejorando la calidad del código.