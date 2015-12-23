# -*- coding: utf-8 -*-

"""
Транспорт для смс
Дополнительные параметры: login, password, var1, var2.
"""

class sms_transport:
    def __init___ (self, login, password, var1, var2):
        self.login = login
        self.password = password
        self.var1 = var1
        self.var2 = var2
    def send(phone, msg):
        print("phone: ", phone, "; message: ", msg)


if __name__ == "__main__":
    sms_transport.send(phone="123123", msg="qweqwe")