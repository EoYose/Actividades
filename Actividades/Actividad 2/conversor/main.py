import tkinter as tk
from tkinter import ttk, messagebox

from dec_bin import dec_bin
from dec_oct import dec_oct
from dec_hex import dec_hex

from bin_dec import bin_dec
from oct_dec import oct_dec
from hex_dec import hex_dec


def convertir():
    valor = entry_valor.get().strip()
    tipo = combo_tipo.get()

    if not valor:
        messagebox.showerror("Error", "Ingresa un valor")
        return

    try:
        if tipo == "Decimal → Binario":
            resultado = dec_bin(int(valor))
        elif tipo == "Decimal → Octal":
            resultado = dec_oct(int(valor))
        elif tipo == "Decimal → Hexadecimal":
            resultado = dec_hex(int(valor))
        elif tipo == "Binario → Decimal":
            resultado = bin_dec(valor)
        elif tipo == "Octal → Decimal":
            resultado = oct_dec(valor)
        elif tipo == "Hexadecimal → Decimal":
            resultado = hex_dec(valor)
        else:
            resultado = "Conversión no válida"

        label_resultado.config(text=f"Resultado: {resultado}")

    except Exception as e:
        messagebox.showerror("Error", f"Entrada inválida\n{e}")


# Ventana principal
root = tk.Tk()
root.title("Conversor de Bases")
root.geometry("350x220")
root.resizable(False, False)

# Título
titulo = tk.Label(root, text="Conversor de Bases Numéricas", font=("Arial", 14))
titulo.pack(pady=10)

# Entrada
entry_valor = tk.Entry(root, width=25, font=("Arial", 12))
entry_valor.pack(pady=5)

# Selector de conversión
combo_tipo = ttk.Combobox(root, state="readonly", width=25)
combo_tipo["values"] = [
    "Decimal → Binario",
    "Decimal → Octal",
    "Decimal → Hexadecimal",
    "Binario → Decimal",
    "Octal → Decimal",
    "Hexadecimal → Decimal"
]
combo_tipo.current(0)
combo_tipo.pack(pady=5)

# Botón
btn_convertir = tk.Button(root, text="Convertir", command=convertir)
btn_convertir.pack(pady=10)

# Resultado
label_resultado = tk.Label(root, text="Resultado: ", font=("Arial", 12))
label_resultado.pack(pady=5)

# Ejecutar
root.mainloop()