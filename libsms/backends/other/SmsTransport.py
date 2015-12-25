# -*- coding: utf-8 -*-

"""
Транспорт для смс
Дополнительные параметры: login, password, var1, var2.
"""

from libsms.backends.basicSms import basicSmsTransport

class smsTransport(basicSmsTransport):
    def __init___ (self, login, password, var1, var2):
        self.login = login
        self.password = password
        self.var1 = var1
        self.var2 = var2



if __name__ == "__main__":
    smsTransport.send(phone="123123", msg="qweqwe")