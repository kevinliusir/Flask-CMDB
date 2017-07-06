#encoding: utf-8
import gconf

import json
def get_users():
    handler = open(gconf.USER_FILE,'rb')
    cxt = handler.read()
    handler.close()
    return json.loads(cxt)

def va_login(username,password):
    return True
