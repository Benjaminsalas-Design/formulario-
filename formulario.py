import re
import tkinter as tk
from tkinter import messagebox


class FormularioRegistro:

  def __init__(self):
    # 1. Ventana principal
    self.root = tk.Tk()
    self.root.title("Registro de Usuario")
    self.root.geometry("460x620")
    self.root.resizable(False, False)

    # 2. Variables de control de los datos
    self.nombre = tk.StringVar()
    self.email = tk.StringVar()
    self.password = tk.StringVar()
    self.confirm = tk.StringVar()
    self.edad = tk.StringVar()
    self.genero = tk.StringVar(value="")
    self.acepto = tk.BooleanVar(value=False)

    # Variables para los mensajes de error individuales junto a cada campo
    self.err_nombre = tk.StringVar()
    self.err_email = tk.StringVar()
    self.err_password = tk.StringVar()
    self.err_confirm = tk.StringVar()
    self.err_edad = tk.StringVar()
    self.err_genero = tk.StringVar()
    self.err_acepto = tk.StringVar()

    # 3. Contenedor principal
    self.frame = tk.Frame(self.root, padx=25, pady=15)
    self.frame.pack(fill="both", expand=True)

    # Título interno (Fila 0)
    tk.Label(self.frame, text="Registro de Usuario", font=("Arial", 16)).grid(
        row=0, column=0, columnspan=2, pady=(0, 12)
    )

    # --- Fila 1 y 2: Nombre completo ---
    tk.Label(self.frame, text="Nombre completo:").grid(
        row=1, column=0, sticky="e", padx=(0, 10)
    )
    self.entry_nombre = tk.Entry(self.frame, textvariable=self.nombre, width=32)
    self.entry_nombre.grid(row=1, column=1, sticky="w")
    self.entry_nombre.focus_set()
    self.entry_nombre.bind(
        "<FocusOut>", lambda e: self.validar_campo("nombre")
    )
    tk.Label(
        self.frame,
        textvariable=self.err_nombre,
        fg="#d32f2f",
        font=("Arial", 8),
    ).grid(row=2, column=1, sticky="w", pady=(0, 4))

    # --- Fila 3 y 4: Email ---
    tk.Label(self.frame, text="Email:").grid(
        row=3, column=0, sticky="e", padx=(0, 10)
    )
    entry_email = tk.Entry(self.frame, textvariable=self.email, width=32)
    entry_email.grid(row=3, column=1, sticky="w")
    entry_email.bind("<FocusOut>", lambda e: self.validar_campo("email"))
    tk.Label(
        self.frame,
        textvariable=self.err_email,
        fg="#d32f2f",
        font=("Arial", 8),
    ).grid(row=4, column=1, sticky="w", pady=(0, 4))

    # --- Fila 5 y 6: Contraseña ---
    tk.Label(self.frame, text="Contraseña:").grid(
        row=5, column=0, sticky="e", padx=(0, 10)
    )
    entry_pass = tk.Entry(
        self.frame, textvariable=self.password, show="*", width=32
    )
    entry_pass.grid(row=5, column=1, sticky="w")
    entry_pass.bind("<FocusOut>", lambda e: self.validar_campo("password"))
    tk.Label(
        self.frame,
        textvariable=self.err_password,
        fg="#d32f2f",
        font=("Arial", 8),
    ).grid(row=6, column=1, sticky="w", pady=(0, 4))

    # --- Fila 7 y 8: Confirmar contraseña ---
    tk.Label(self.frame, text="Confirmar:").grid(
        row=7, column=0, sticky="e", padx=(0, 10)
    )
    entry_conf = tk.Entry(
        self.frame, textvariable=self.confirm, show="*", width=32
    )
    entry_conf.grid(row=7, column=1, sticky="w")
    entry_conf.bind("<FocusOut>", lambda e: self.validar_campo("confirm"))
    tk.Label(
        self.frame,
        textvariable=self.err_confirm,
        fg="#d32f2f",
        font=("Arial", 8),
    ).grid(row=8, column=1, sticky="w", pady=(0, 4))

    # --- Fila 9 y 10: Edad ---
    tk.Label(self.frame, text="Edad:").grid(
        row=9, column=0, sticky="e", padx=(0, 10)
    )
    entry_edad = tk.Entry(self.frame, textvariable=self.edad, width=10)
    entry_edad.grid(row=9, column=1, sticky="w")
    entry_edad.bind("<FocusOut>", lambda e: self.validar_campo("edad"))
    tk.Label(
        self.frame,
        textvariable=self.err_edad,
        fg="#d32f2f",
        font=("Arial", 8),
    ).grid(row=10, column=1, sticky="w", pady=(0, 4))

    # --- Fila 11 y 12: Género ---
    tk.Label(self.frame, text="Género:").grid(
        row=11, column=0, sticky="ne", padx=(0, 10)
    )
    gf = tk.Frame(self.frame)
    gf.grid(row=11, column=1, sticky="w")
    for txt in ["Masculino", "Femenino", "Otro"]:
      tk.Radiobutton(
          gf,
          text=txt,
          variable=self.genero,
          value=txt,
          command=lambda: self.validar_campo("genero"),
      ).pack(anchor="w")
    tk.Label(
        self.frame,
        textvariable=self.err_genero,
        fg="#d32f2f",
        font=("Arial", 8),
    ).grid(row=12, column=1, sticky="w", pady=(0, 4))

    # --- Fila 13 y 14: Checkbox Acepto términos ---
    self.chk_acepto = tk.Checkbutton(
        self.frame,
        text="Acepto términos y condiciones",
        variable=self.acepto,
        command=lambda: self.validar_campo("acepto"),
    )
    self.chk_acepto.grid(row=13, column=0, columnspan=2, pady=(8, 0))
    tk.Label(
        self.frame,
        textvariable=self.err_acepto,
        fg="#d32f2f",
        font=("Arial", 8),
    ).grid(row=14, column=0, columnspan=2, pady=(0, 10))

    # Accesibilidad: Enter envía el formulario
    self.chk_acepto.bind("<Return>", lambda event: self.validar_todo())
    self.root.bind("<Return>", lambda event: self.validar_todo())

    # --- Fila 15: Botones Registrar y Limpiar ---
    bf = tk.Frame(self.frame)
    bf.grid(row=15, column=0, columnspan=2, pady=8)

    tk.Button(
        bf, text="Registrar", command=self.validar_todo, width=15, bg="#c8e6c9"
    ).pack(side="left", padx=10)
    tk.Button(
        bf, text="Limpiar", command=self.limpiar, width=15, bg="#f8bbd0"
    ).pack(side="left", padx=10)

  def validar_campo(self, campo):
    """Valida un campo individual y muestra su error específico debajo."""
    if campo == "nombre":
      if not self.nombre.get().strip():
        self.err_nombre.set("Campo obligatorio: ingresa tu nombre completo.")
        return "Nombre completo: es obligatorio."
      self.err_nombre.set("")

    elif campo == "email":
      email_val = self.email.get().strip()
      if not email_val:
        self.err_email.set("Campo obligatorio: ingresa un correo.")
        return "Email: es obligatorio."
      elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_val):
        self.err_email.set("Error de formato: debe incluir '@' y '.'")
        return "Email: error de formato (debe incluir '@' y '.')."
      self.err_email.set("")

    elif campo == "password":
      if len(self.password.get()) < 8:
        self.err_password.set("Mínimo 8 caracteres requeridos.")
        return "Contraseña: debe tener al menos 8 caracteres."
      self.err_password.set("")

    elif campo == "confirm":
      if not self.confirm.get():
        self.err_confirm.set("Debes confirmar tu contraseña.")
        return "Confirmar contraseña: campo obligatorio."
      elif self.password.get() != self.confirm.get():
        self.err_confirm.set("Error de coincidencia: las contraseñas no son iguales.")
        return "Confirmar contraseña: error de coincidencia."
      self.err_confirm.set("")

    elif campo == "edad":
      edad_txt = self.edad.get().strip()
      if not edad_txt:
        self.err_edad.set("Campo obligatorio: ingresa tu edad.")
        return "Edad: es obligatoria."
      elif not edad_txt.isdigit():
        self.err_edad.set("Error numérico: ingresa solo números (ej. 20).")
        return "Edad: error numérico (solo se permiten números)."
      elif int(edad_txt) < 15 or int(edad_txt) > 99:
        self.err_edad.set("Rango inválido: debe ser entre 15 y 99 años.")
        return "Edad: debe estar entre 15 y 99 años."
      self.err_edad.set("")

    elif campo == "genero":
      if not self.genero.get():
        self.err_genero.set("Selecciona una opción de género.")
        return "Género: debes seleccionar una opción."
      self.err_genero.set("")

    elif campo == "acepto":
      if not self.acepto.get():
        self.err_acepto.set("Debes marcar la casilla para continuar.")
        return "Términos y condiciones: debes aceptarlos."
      self.err_acepto.set("")

    return None

  def validar_todo(self):
    """Ejecuta todas las validaciones al presionar Registrar."""
    campos = [
        "nombre",
        "email",
        "password",
        "confirm",
        "edad",
        "genero",
        "acepto",
    ]
    errores = []

    for c in campos:
      error = self.validar_campo(c)
      if error:
        errores.append(f"• {error}")

    if errores:
      messagebox.showerror(
          "Errores en el formulario",
          "Revisa los campos marcados en rojo:\n\n" + "\n".join(errores),
      )
    else:
      messagebox.showinfo(
          "Registro Exitoso",
          f"¡Bienvenido, {self.nombre.get().strip()}!\nTu registro se completó"
          " correctamente.",
      )
      self.limpiar()

  def limpiar(self):
    """Resetea todos los campos y borra todos los mensajes de error."""
    self.nombre.set("")
    self.email.set("")
    self.password.set("")
    self.confirm.set("")
    self.edad.set("")
    self.genero.set("")
    self.acepto.set(False)

    # Limpiar textos rojos
    self.err_nombre.set("")
    self.err_email.set("")
    self.err_password.set("")
    self.err_confirm.set("")
    self.err_edad.set("")
    self.err_genero.set("")
    self.err_acepto.set("")

    self.entry_nombre.focus_set()


if __name__ == "__main__":
  app = FormularioRegistro()
  app.root.mainloop()
  