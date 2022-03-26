# from typing import Any
from urllib import response
import requests
import pandas as pd
# import json
# from flask import jsonify

def get_kpi1():
    response = requests.get("https://g2357549164ffb0-dbtipsession3k.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi1/incvol/")
    return response.json()

def get_kpi2():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi2/incsolved/")
    return response.json()

def get_kpi3():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi3/inccrit/")
    return response.json()

def get_kpi4():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi4/inccause/")
    return response.json()

def get_kpi5():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi5/incSLAcrit/")
    return response.json()

def get_kpi6():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi6/incSLAalt/")
    return response.json()

def get_kpi7():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi7/incSLAmed/")
    return response.json()

def get_kpi8():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi8/incSLAbaj/")
    return response.json()

def get_kpi9():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi9/AVGSLA/")
    return response.json()

def get_kpi10():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi10/avgtinc/")
    return response.json()

def get_kpi11():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi11/avgtimebaja/")
    return response.json()

def get_kpi12():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi12/avgtimemed/")
    return response.json()

def get_kpi13():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi13/avgtimealta/")
    return response.json()

def get_kpi14():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi14/avgcritnon/")
    return response.json()

def get_kpi15():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi15/avgaltanon/")
    return response.json()

def get_kpi16():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi16/avgmednon/")
    return response.json()

def get_kpi17():
    response = requests.get("https://g2357549164ffb0-db202203091212.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi17/avgbajnon/")
    return response.json()







# def kpi1(data_json):
#     data_json = requests.get("https://g2357549164ffb0-dbtipsession3k.adb.eu-frankfurt-1.oraclecloudapps.com/ords/tip/kpi1/incvol/")
#     data=json.loads(data_json.content)
#     key_data=data['items']
#     kpi1= jsonify(key_data)

#     return data_json


# df_kpi1 = pd.DataFrame(["items"])

