import pandas as pd

def txt_to_excel(input_file, output_file, delimiter, encoding, has_header, sheet_name):
    if not delimiter:
        delimiter = '\t'  # Por defecto, tabulador

    header = 0 if has_header.lower() in ('yes', 'true', '1') else None
    df = pd.read_csv(input_file, sep=delimiter, header=header, encoding=encoding)
    df.to_excel(output_file, sheet_name=sheet_name, index=False)
