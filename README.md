# Práctica Guiada: Interfaces Gráficas (GUI) en Python con Tkinter

Este repositorio contiene los entregables correspondientes a la sesión práctica sobre diseño de interfaces gráficas de usuario (GUI), usabilidad, accesibilidad y validación de formularios en Python utilizando la librería estándar `tkinter`.

**Autor:** Benjamín Salas (`Benjaminsalas-Design`)

---

##  Estructura del Proyecto

* `wireframe.png`: Boceto estructural previo al desarrollo del formulario, planificando la jerarquía visual, distribución en cuadrícula y paleta de colores.
* `formulario.py`: Aplicación de escritorio de registro de usuarios con validación en tiempo real junto a cada campo y retroalimentación clara.
* `calculadora.py`: Aplicación de demostración desarrollada en clase aplicando layouts con `grid()`, programación orientada a objetos (POO) y manejo de excepciones.
* `README.md`: Documentación del diseño y funcionamiento del proyecto.

---

##  Decisiones de Diseño y Usabilidad (`formulario.py`)

El desarrollo partió desde la fase de bocetado (`wireframe.png`) antes de escribir código, aplicando los siguientes principios de interfaz:

1. **Distribución y Jerarquía Visual (`grid()`):**
   * Título principal centrado en la parte superior para contextualizar la tarea.
   * Estructura de dos columnas alineadas: etiquetas descriptivas alineadas a la derecha (`sticky="e"`) y controles de entrada alineados a la izquierda (`sticky="w"`), facilitando la lectura rápida.
   * Opciones de género (`Radiobutton`) apiladas verticalmente para evitar saturación horizontal y mejorar la precisión de selección.
2. **Consistencia Visual y Código de Color:**
   * Botones diferenciados semánticamente con tonos suaves: **Registrar** en verde (`#c8e6c9`) para la acción principal y **Limpiar** en rosado (`#f8bbd0`) para el reinicio del formulario.
3. **Prevención de Errores y Retroalimentación Inmediata:**
   * Validación individual al perder el foco (`<FocusOut>`) y validación global al enviar.
   * Mensajes de error específicos en color rojo ubicados directamente debajo de cada campo inválido, acompañados de un resumen emergente (`messagebox`) en caso de múltiples errores.
   * Ocultamiento de caracteres (`show="*"`) en los campos de contraseña.
4. **Accesibilidad:**
   * Enfoque automático (`focus_set()`) en el primer campo al iniciar la ventana.
   * Orden lógico de tabulación (`Tab`) recorriendo todos los controles de arriba hacia abajo.
   * Envío directo del formulario mediante la tecla `Enter` (`<Return>`).

---

##  Reglas de Validación y Casos de Prueba

El formulario verifica el cumplimiento de las siguientes reglas antes de permitir el registro:

* **Campos obligatorios:** Ningún campo puede quedar vacío o contener solo espacios.
* **Formato de correo electrónico:** Validación mediante expresión regular verificando la presencia de `@` y `.` (`usuario@dominio.com`).
* **Seguridad y coincidencia de contraseña:** Longitud mínima de 8 caracteres y verificación exacta con el campo de confirmación.
* **Edad numérica:** Solo acepta valores numéricos enteros dentro del rango válido de **15 a 99 años**.
* **Selección y términos:** Requiere elegir una opción de género y marcar la casilla de aceptación de términos y condiciones.

---

##  Cómo ejecutar las aplicaciones

Asegúrate de tener **Python 3.x** instalado en tu sistema (la librería `tkinter` viene incluida por defecto).

1. Clona este repositorio:
   ```bash
   git clone [https://github.com/Benjaminsalas-Design/formulario-.git](https://github.com/Benjaminsalas-Design/formulario-.git)