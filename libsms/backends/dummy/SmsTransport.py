# -*- coding: utf-8 -*-

"""
Транспорт для смс
Дополнительные параметры: отсутствуют
"""

class sms_transport:
    def send(phone, msg):
        print("phone: ", phone, "; message: ", msg)

if __name__ == "__main__":
    sms_transport.send(phone="123123", msg="qweqwe")
