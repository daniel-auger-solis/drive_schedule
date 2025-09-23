from __future__ import print_function
import datetime
import os.path
import gspread
from google.oauth2.service_account import Credentials

# Credenciales y archivos
credentials_sheet_drive = "geminiapi-470823-262f80dddb02.json"
SPREADSHEET_ID = "1ZWqpLUSZ0QuHAJf4vb48JCP-kYSlXGz7BqMybk7KHgI"

# Alcances necesarios para Google Sheets y Drive
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

# Cargar credenciales desde un archivo JSON descargado de Google Cloud
creds = Credentials.from_service_account_file(credentials_sheet_drive, scopes=SCOPES)

# Conectar con Google Sheets
client = gspread.authorize(creds)

# Abrir la primera hoja
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

# Contar filas existentes
values = sheet.get_all_values()

if not values:
    # Hoja vacía → empezar con 1
    next_action_number = 1
else:
    # Buscar la última acción escrita
    last_row = values[-1]
    if last_row and last_row[0].startswith("Accion"):
        # Extraer el número después de "Accion"
        try:
            last_number = int(last_row[0].split()[1])
            next_action_number = last_number + 1
        except (IndexError, ValueError):
            next_action_number = len(values)  # fallback
    else:
        next_action_number = len(values)  # fallback

accion = f"Accion {next_action_number}"
fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

sheet.append_row([accion, fecha])
print(f"Agregado: {accion} - {fecha}")