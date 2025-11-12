[Setup]
AppName=Convertidor TXT a Excel
AppVersion=1.0
DefaultDirName={autopf}\ConvertidorTXTExcel
DefaultGroupName=Convertidor TXT a Excel
OutputDir=.
OutputBaseFilename=Instalador_txt2excel
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\txt2excel.exe"; DestDir: "{app}"
Source: "config.ini"; DestDir: "{app}"
Source: "sample_input.txt"; DestDir: "{app}"

[Icons]
Name: "{group}\Convertidor TXT a Excel"; Filename: "{app}\txt2excel.exe"
Name: "{commondesktop}\Convertidor TXT a Excel"; Filename: "{app}\txt2excel.exe"

[Run]
Filename: "{app}\txt2excel.exe"; Description: "Ejecutar la aplicación"; Flags: nowait postinstall skipifsilent
