import tkinter as tk
from tkinter import filedialog, messagebox
import configparser
import converter
import os

CONFIG_FILE = "config.ini"

def cargar_config():
    cfg = configparser.ConfigParser()
    cfg.read(CONFIG_FILE, encoding="utf-8")
    c = cfg["TXT2XLSX"]
    return {
        "delimiter": c.get("delimiter", "\t"),
        "encoding": c.get("encoding", "utf-8"),
        "has_header": c.get("has_header", "yes"),
        "sheet_name": c.get("sheet_name", "Sheet1")
    }

def guardar_config(nueva_config):
    cfg = configparser.ConfigParser()
    cfg["TXT2XLSX"] = nueva_config
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        cfg.write(f)

def abrir_config():
    config = cargar_config()

    ventana_conf = tk.Toplevel(root)
    ventana_conf.title("Configuración")
    ventana_conf.geometry("350x250")

    tk.Label(ventana_conf, text="Delimitador:").pack(pady=5)
    delimiter_var = tk.StringVar(value=config["delimiter"])
    delimiter_entry = tk.Entry(ventana_conf, textvariable=delimiter_var, width=30)
    delimiter_entry.pack()

    tk.Label(ventana_conf, text="Codificación (encoding):").pack(pady=5)
    encoding_var = tk.StringVar(value=config["encoding"])
    encoding_entry = tk.Entry(ventana_conf, textvariable=encoding_var, width=30)
    encoding_entry.pack()

    tk.Label(ventana_conf, text="Tiene encabezado (yes/no):").pack(pady=5)
    header_var = tk.StringVar(value=config["has_header"])
    header_entry = tk.Entry(ventana_conf, textvariable=header_var, width=30)
    header_entry.pack()

    tk.Label(ventana_conf, text="Nombre de hoja Excel:").pack(pady=5)
    sheet_var = tk.StringVar(value=config["sheet_name"])
    sheet_entry = tk.Entry(ventana_conf, textvariable=sheet_var, width=30)
    sheet_entry.pack()

    def guardar_y_cerrar():
        nueva_conf = {
            "delimiter": delimiter_var.get(),
            "encoding": encoding_var.get(),
            "has_header": header_var.get(),
            "sheet_name": sheet_var.get()
        }
        guardar_config(nueva_conf)
        messagebox.showinfo("Configuración", "Configuración guardada correctamente.")
        ventana_conf.destroy()

    tk.Button(ventana_conf, text="Guardar", command=guardar_y_cerrar, bg="#2196F3", fg="white").pack(pady=10)

def convertir():
    try:
        config = cargar_config()
        input_path = entrada_txt.get()
        output_path = salida_xlsx.get()

        if not os.path.exists(input_path):
            messagebox.showerror("Error", "Archivo TXT no encontrado.")
            return

        converter.txt_to_excel(
            input_path,
            output_path,
            config["delimiter"],
            config["encoding"],
            config["has_header"],
            config["sheet_name"]
        )

        messagebox.showinfo("Éxito", f"Archivo convertido correctamente:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def seleccionar_txt():
    path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if path:
        entrada_txt.set(path)

def seleccionar_destino():
    path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                        filetypes=[("Archivos Excel", "*.xlsx")])
    if path:
        salida_xlsx.set(path)

# --- Interfaz principal ---
root = tk.Tk()
root.title("Convertidor TXT a Excel")
root.geometry("420x300")

entrada_txt = tk.StringVar()
salida_xlsx = tk.StringVar()

# Botón configuración arriba
tk.Button(root, text="⚙️ Configuración", command=abrir_config, bg="#607D8B", fg="white").pack(pady=10)

tk.Label(root, text="Archivo TXT:").pack(pady=5)
tk.Entry(root, textvariable=entrada_txt, width=50).pack()
tk.Button(root, text="Buscar...", command=seleccionar_txt).pack(pady=5)

tk.Label(root, text="Archivo de salida XLSX:").pack(pady=5)
tk.Entry(root, textvariable=salida_xlsx, width=50).pack()
tk.Button(root, text="Guardar como...", command=seleccionar_destino).pack(pady=5)

tk.Button(root, text="Convertir", command=convertir, bg="#4CAF50", fg="white").pack(pady=15)

root.mainloop()
