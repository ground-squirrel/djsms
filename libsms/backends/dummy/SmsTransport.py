# -*- coding: utf-8 -*-

"""
Транспорт для смс
Дополнительные параметры: отсутствуют
"""

from libsms.backends.basicSms import basicSmsTransport

class smsTransport(basicSmsTransport):
    pass

if __name__ == "__main__":
    smsTransport.send(phone="123123", msg="qweqwe")
