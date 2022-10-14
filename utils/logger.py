import json

def logger_json(value):
    f = open('logs/holamundo.txt','w')
    json.dump(value, f, indent = 6)
    f.close()


def logger_txt(value):
    f = open('logs/holamundo.txt','w')
    f.write(value)
    f.close()