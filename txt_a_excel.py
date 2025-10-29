#!/usr/bin/env python3
"""
txt_to_excel.py
Convierte archivos TXT a Excel (.xlsx) usando configuración desde ini o xml.
Uso: python txt_to_excel.py --input archivo.txt --config config.ini
"""

import argparse
import configparser
import xml.etree.ElementTree as ET
import logging
import sys
from pathlib import Path
import pandas as pd

# --- Logging ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# --- Helpers para config ---
def read_ini(path):
    cfg = configparser.ConfigParser()
    cfg.read(path, encoding='utf-8')
    options = cfg['app'] if 'app' in cfg else cfg.defaults()
    return dict(options)

def read_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    options = {}
    for child in root:
        options[child.tag] = child.text
    return options

def parse_bool(val):
    if val is None: return False
    return str(val).lower() in ('1','true','yes','y')

# --- Lectura de TXT según config ---
def load_txt(path, cfg):
    path = Path(path)
    sep = cfg.get('sep')
    encoding = cfg.get('encoding', 'utf-8')
    header = None if cfg.get('header','none').lower() in ('none','no') else int(cfg.get('header', 0))
    skiprows = int(cfg.get('skiprows', 0))
    engine = cfg.get('engine', None)
    file_type = cfg.get('file_type','delimited')

    logging.info(f"Loading {path} as {file_type} (encoding={encoding})")

    if file_type == 'fwf':
        widths = cfg.get('widths')
        if not widths:
            raise ValueError("Para file_type=fwf debe indicarse widths en config (ej: widths=10,5,20)")
        widths = [int(x.strip()) for x in widths.split(',')]
        df = pd.read_fwf(path, widths=widths, header=header, skiprows=skiprows, encoding=encoding)
    else:
        if sep is None or sep.lower() == 'auto':
            df = pd.read_csv(path, sep=None, engine='python', header=header, skiprows=skiprows, encoding=encoding)
        else:
            df = pd.read_csv(path, sep=sep, header=header, skiprows=skiprows, encoding=encoding, engine=engine)
    return df

def apply_transformations(df, cfg):
    rename_map = cfg.get('rename_columns')
    if rename_map:
        pairs = [p.strip() for p in rename_map.split(',') if p.strip()]
        mapping = {}
        for p in pairs:
            old,new = p.split(':')
            mapping[old.strip()] = new.strip()
        df = df.rename(columns=mapping)
    if parse_bool(cfg.get('drop_empty_columns','false')):
        df = df.dropna(axis=1, how='all')
    return df

def main():
    parser = argparse.ArgumentParser(description="Convert TXT to Excel")
    parser.add_argument('--input', '-i', required=True, help='Archivo TXT de entrada')
    parser.add_argument('--output', '-o', help='Archivo XLSX de salida (opcional)')
    parser.add_argument('--config', '-c', help='Archivo de configuración (ini o xml)')
    parser.add_argument('--sep', help='Separador (anula config)')
    args = parser.parse_args()

    cfg = {}
    if args.config:
        cfgpath = Path(args.config)
        if not cfgpath.exists():
            logging.error("Config file not found: %s", cfgpath)
            sys.exit(1)
        if cfgpath.suffix.lower() in ('.ini', '.cfg'):
            cfg = read_ini(cfgpath)
        elif cfgpath.suffix.lower() in ('.xml',):
            cfg = read_xml(cfgpath)
        else:
            logging.error("Formato de config no soportado. Use .ini o .xml")
            sys.exit(1)

    if args.sep:
        cfg['sep'] = args.sep

    try:
        df = load_txt(args.input, cfg)
        df = apply_transformations(df, cfg)
    except Exception as e:
        logging.exception("Error al leer/transformar")
        sys.exit(2)

    out = args.output or (Path(args.input).with_suffix('.xlsx'))
    logging.info(f"Guardando Excel en: {out}")
    try:
        df.to_excel(out, index=False, engine='openpyxl')
    except Exception as e:
        logging.exception("Error al guardar Excel")
        sys.exit(3)
    logging.info("Conversión finalizada con éxito.")

    # --- Mantener la ventana abierta ---
    input("¡Conversión terminada! Presioná Enter para cerrar...")

if __name__ == '__main__':
    main()
