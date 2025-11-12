# Guía para generar el ejecutable (.exe) en Windows

Este documento explica cómo crear el archivo ejecutable (.exe) de la aplicación Convertidor TXT a Excel, cumpliendo con el requisito de “Aplicación Win32”.

## Requisitos previos

1. Tener instalado Python 3.11 (32 bits)
2. Haber creado y activado el entorno virtual (env)
3. Tener en la carpeta FINAL los archivos:
   - app.py
   - converter.py
   - config.ini
   - requirements.txt
   - Dockerfile
   - build-windows.md
   - sample_input.txt

## Paso 1: Activar el entorno virtual

Abrí PowerShell en la carpeta FINAL y ejecutá:

cd "C:\Users\003\Desktop\FINAL"
.\env\Scripts\Activate.ps1


Debe verse algo así:

(env) PS C:\Users\003\Desktop\FINAL>


## Paso 2: Instalar PyInstaller

Instalá PyInstaller con:

pip install pyinstaller


## Paso 3: Crear el ejecutable

Ejecutá este comando:

pyinstaller --onefile --windowed --name txt2excel app.py


## Paso 4: Ubicación del ejecutable

El archivo se crea en:

C:\Users\003\Desktop\FINAL\dist\txt2excel.exe


Abrilo con doble clic para usar el convertidor.

## Paso 5: Probar el ejecutable

1. Copiá `sample_input.txt` junto al `.exe`
2. Abrí `txt2excel.exe`
3. Elegí el TXT → seleccioná `sample_input.txt`
4. Guardá como `resultado.xlsx`
5. Tocá “Convertir”

Si todo está bien, mostrará el mensaje “Archivo convertido correctamente”.

## Paso 6: Crear instalador (opcional)

Podés usar:
- Inno Setup → https://jrsoftware.org/isinfo.php
- NSIS → https://nsis.sourceforge.io/Download

No es obligatorio.

## Resultado final

✅ Aplicación de escritorio (Tkinter)  
✅ Ejecutable Win32 (`txt2excel.exe`)  
✅ Código fuente incluido  
✅ Configuración editable (`config.ini`)  
✅ Compatible con Docker  
✅ Proyecto completo listo para entrega 🎓












