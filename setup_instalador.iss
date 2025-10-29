; Script de instalación para txt_a_excel
[Setup]
AppName=Conversor TXT a Excel
AppVersion=1.0
DefaultDirName={autopf}\Conversor TXT a Excel
DefaultGroupName=Conversor TXT a Excel
OutputBaseFilename=Instalador_TXT_a_Excel
Compression=lzma
SolidCompression=yes

[Files]
; Copia el ejecutable y el config
Source: "dist\txt_a_excel.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "config.ini"; DestDir: "{app}"; Flags: ignoreversion
Source: "datos.txt"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Conversor TXT a Excel"; Filename: "{app}\txt_a_excel.exe"
Name: "{commondesktop}\Conversor TXT a Excel"; Filename: "{app}\txt_a_excel.exe"

[Run]
Filename: "{app}\txt_a_excel.exe"; Description: "Ejecutar Conversor TXT a Excel"; Flags: nowait postinstall skipifsilent
