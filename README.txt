TXT a Excel

DESCRIPCIÓN
Esta aplicación convierte archivos de texto (.txt) en archivos Excel (.xlsx) de manera sencilla y configurable.
Permite definir el separador de columnas, encabezados, filas a saltar, renombrar columnas y eliminar columnas vacías mediante un archivo de configuración (config.ini).

La app está programada en Python y también se distribuye como ejecutable para Windows (.exe).
Opcionalmente, se puede crear un contenedor Docker o un instalador con Inno Setup.

ESTRUCTURA DEL PROYECTO

Proyecto/
│
├─ txt_a_excel.py         Código fuente en Python
├─ txt_a_excel.exe        Ejecutable Windows (generado con PyInstaller)
├─ config.ini             Archivo de configuración de la app
├─ requirements.txt       Librerías necesarias para Python
├─ datos.txt              Archivo de ejemplo de entrada
├─ datos.xlsx             Archivo de ejemplo de salida
├─ Dockerfile             Opcional, para contenedor Docker
├─ setup_instalador.iss   Opcional, script de Inno Setup para instalador
└─ README.txt             Este archivo

REQUISITOS

- Windows 32/64-bit para ejecutar el EXE.
- Python 3.13 o superior (si se quiere ejecutar desde código fuente).
- Librerías: pandas, openpyxl.
- Opcional: Docker e Inno Setup si se desea contenedor o instalador.

INSTALACIÓN Y EJECUCIÓN DESDE CÓDIGO FUENTE

1. Crear y activar un entorno virtual:

python -m venv venv
.\venv\Scripts\Activate

2. Instalar dependencias:

pip install -r requirements.txt

3. Ejecutar la app:

python txt_a_excel.py -i datos.txt

Esto generará datos.xlsx en la misma carpeta que el TXT de entrada.

USO DEL EXE (WINDOWS)

1. Ir a la carpeta dist en PowerShell:

cd dist

2. Ejecutar el EXE apuntando al archivo TXT:

.\txt_a_excel.exe -i ..\datos.txt

El resultado será datos.xlsx en la carpeta principal del proyecto.

CONFIGURACIÓN (config.ini)

Se pueden modificar los parámetros de la conversión:

[app]
sep = \t                   Separador de columnas (\t = tab, , = coma, ; = punto y coma)
encoding = utf-8           Codificación del archivo
header = 0                 Fila de encabezado (0 = primera fila)
skiprows = 0               Filas a saltar al inicio
rename_columns =           Renombrar columnas: viejo1:nuevo1,viejo2:nuevo2
drop_empty_columns = false Eliminar columnas vacías

Si tu TXT usa tabulador, no hace falta cambiar nada.

EJEMPLOS

Archivo de entrada datos.txt:

nombre	apellido	edad
Brian	Caceres	18
Ana	    Perez	25

Resultado datos.xlsx:
Archivo Excel con las mismas columnas y datos.

OPCIONALES

- Docker: se puede generar un contenedor que instale dependencias y ejecute la app.
- Instalador: se puede crear un .exe de instalación con Inno Setup usando setup_instalador.iss.

AUTOR

Brian Cáceres
Estudiante de programación












