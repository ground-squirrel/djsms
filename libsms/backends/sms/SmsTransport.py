# -*- coding: utf-8 -*-

"""
Транспорт для смс
Дополнительные параметры: login, password.
"""

from libsms.backends.basicSms import basicSmsTransport

class smsTransport(basicSmsTransport):
    def __init___ (login, password):
        self.login = login
        self.password = password


if __name__ == "__main__":
    smsTransport.send(phone="123123", msg="qweqwe")