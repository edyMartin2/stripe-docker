from flask import request 
from utils.logger import logger_txt, logger_json

def webhook_v1():
    record = request.get_json()
    headers = request.headers['STRIPE_SIGNATURE']
    logger_json(record)
    logger_txt(headers)    
    return headers