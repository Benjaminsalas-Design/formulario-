import tkinter as tk
from tkinter import messagebox


class Calculadora:

  def __init__(self):
    # 1. Configuración de la ventana principal
    self.root = tk.Tk()
    self.root.title("Calculadora")
    self.root.geometry("320x420")
    self.root.resizable(False, False)

    # Variable que almacena la expresión matemática actual
    self.expresion = ""
    self.texto_pantalla = tk.StringVar()

    # 2. Pantalla de resultados (Entry alineado a la derecha y solo lectura)
    pantalla = tk.Entry(
        self.root,
        textvariable=self.texto_pantalla,
        font=("Arial", 22, "bold"),
        justify="right",
        bd=10,
        relief="sunken",
        state="readonly",
    )
    pantalla.grid(
        row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew"
    )

    # 3. Distribución de botones en cuadrícula (texto, fila, columna)
    botones = [
        ("7", 1, 0),
        ("8", 1, 1),
        ("9", 1, 2),
        ("/", 1, 3),
        ("4", 2, 0),
        ("5", 2, 1),
        ("6", 2, 2),
        ("*", 2, 3),
        ("1", 3, 0),
        ("2", 3, 1),
        ("3", 3, 2),
        ("-", 3, 3),
        ("C", 4, 0),
        ("0", 4, 1),
        ("=", 4, 2),
        ("+", 4, 3),
    ]

    # Crear botones dinámicamente
    for texto, fila, columna in botones:
      if texto == "=":
        btn = tk.Button(
            self.root,
            text=texto,
            font=("Arial", 16, "bold"),
            bg="#c8e6c9",
            command=self.calcular,
        )
      elif texto == "C":
        btn = tk.Button(
            self.root,
            text=texto,
            font=("Arial", 16, "bold"),
            bg="#f8bbd0",
            command=self.limpiar,
        )
      elif texto in ["/", "*", "-", "+"]:
        btn = tk.Button(
            self.root,
            text=texto,
            font=("Arial", 16, "bold"),
            bg="#e0e0e0",
            command=lambda t=texto: self.presionar(t),
        )
      else:
        btn = tk.Button(
            self.root,
            text=texto,
            font=("Arial", 16),
            command=lambda t=texto: self.presionar(t),
        )

      btn.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

    # 4. Configurar peso de filas y columnas para que todos los botones tengan el mismo tamaño
    for i in range(1, 5):
      self.root.grid_rowconfigure(i, weight=1)
    for j in range(4):
      self.root.grid_columnconfigure(j, weight=1)

    # Accesibilidad: soporte para teclado físico (Enter para calcular, Escape para limpiar)
    self.root.bind("<Return>", lambda event: self.calcular())
    self.root.bind("<Escape>", lambda event: self.limpiar())

  def presionar(self, valor):
    # Evita poner dos operadores seguidos (ej. "++", "*/")
    if (
        valor in "+-*/"
        and self.expresion
        and self.expresion[-1] in "+-*/"
    ):
      self.expresion = self.expresion[:-1] + valor
    else:
      self.expresion += str(valor)
    self.texto_pantalla.set(self.expresion)

  def limpiar(self):
    self.expresion = ""
    self.texto_pantalla.set("")

  def calcular(self):
    if not self.expresion:
      return
    try:
      # eval() evalúa la operación matemática en texto
      resultado = str(eval(self.expresion))
      self.texto_pantalla.set(resultado)
      self.expresion = resultado
    except ZeroDivisionError:
      messagebox.showerror("Error matemático", "No se puede dividir entre cero.")
      self.limpiar()
    except Exception:
      messagebox.showerror("Error de sintaxis", "Expresión inválida.")
      self.limpiar()


if __name__ == "__main__":
  app = Calculadora()
  app.root.mainloop()
  