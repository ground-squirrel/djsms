# -*- coding: utf-8 -*-

"""
Транспорт для смс
Дополнительные параметры: login, password.
"""
class sms_transport:
    def __init___ (self, login, password):
        self.login = login
        self.password = password
    def send(phone, msg):
        print("phone: ", phone, "; message: ", msg)

if __name__ == "__main__":
    sms_transport.send(phone="123123", msg="qweqwe")