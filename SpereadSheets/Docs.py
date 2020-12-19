# link para tutorial: https://www.linkedin.com/pulse/manipulando-planilhas-do-google-usando-python-renan-pessoa/?originalSubdomain=pt

import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

#Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'chave.json', scope)

#Se autentica
gc = gspread.authorize(credentials)

#Abre a planilha
wks = gc.open_by_key('1XnvLH1r8g1P6m0uh_UgCm8GB_38cjMKiwt1wnwAQtIQ') 

#Seleciona a primeira página da planilha
worksheet = wks.get_worksheet(0)

#Atualiza celula
worksheet.update_acell('A1', 'Planilha acessada com sucesso')
