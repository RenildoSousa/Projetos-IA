import requests
from random import randint
import time
contador =0
while (contador < 10):
 contador = contador + 1
 valor = randint(0, 100) 
 r = requests.get("https://script.google.com/macros/s/1XnvLH1r8g1P6m0uh_UgCm8GB_38cjMKiwt1wnwAQtIQ/exec?temperatura="+str(valor))
 time.sleep(1)
 print r.headers['content-type']
 print r.text