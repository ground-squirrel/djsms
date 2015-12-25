# -*- coding: utf-8 -*-

"""
Абстрактный класс транспорта
"""

import abc

class basicSmsTransport:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def send(phone, msg):
        print("phone: ", phone, "; message: ", msg)


