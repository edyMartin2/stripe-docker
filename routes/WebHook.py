from flask import request
import json 

def logger(value):
    f = open('logs/holamundo.txt','w')
    json.dump(value, f, indent = 6)
    f.close()

def webhook_v1():
    record = request.get_json()
    logger(record)    
    return "Hola mundo"