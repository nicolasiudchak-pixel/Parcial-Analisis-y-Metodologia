# SmartGastro - Sistema de Gestión para Foodtrucks 🍔☁️

**SmartGastro** es un prototipo de motor lógico diseñado para optimizar la operación de foodtrucks. El sistema integra la gestión de inventario, ventas y clientes con un enfoque en la prevención de pérdidas y la eficiencia operativa.

Este proyecto forma parte de la primera entrega de la materia **Análisis de Sistemas** (Escuela Da Vinci).

## 🚀 Funcionalidades Principales

*   **Gestión de Inventario**: Alta de productos con control de precios y existencias iniciales.
*   **Control de Ventas (Pedidos)**: Registro de transacciones vinculadas a clientes específicos, con cálculo automático de totales.
*   **Encapsulamiento y Seguridad**: El stock de los productos no puede ser modificado directamente; se utiliza un método validado (`set_stock`) que impide ventas si no hay disponibilidad suficiente.
*   **Base de Datos Relacional**: Estructura preparada para escalabilidad mediante un modelo Entidad-Relación que vincula Clientes, Pedidos y Productos.

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje**: Python 3.x[cite: 1].
*   **Paradigma**: Programación Orientada a Objetos (POO)[cite: 1].
*   **Modelado**: UML 2.0 y Diagramas Entidad-Relación (DER)[cite: 1].

## 📋 Requisitos Técnicos

Para ejecutar este script, solo necesitás tener instalado Python en tu sistema. No requiere dependencias externas adicionales.

## 💻 Instrucciones de Ejecución

1. **Clonar el repositorio**:
   ```bash
   git clone [https://github.com/tu-usuario/smartgastro.git](https://github.com/tu-usuario/smartgastro.git)
