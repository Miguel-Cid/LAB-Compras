from datetime import datetime

def parsear_fecha(string):
    return datetime.strptime(string,"%d/%m/%Y %H:%M")