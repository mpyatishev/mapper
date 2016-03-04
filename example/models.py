# -*- coding: utf-8 -*-

import pprint


class Model:
    def __init__(self, **kwargs):
        for attr, val in kwargs.items():
            self.__setattr__(attr, val)

    def save(self):
        pprint.pprint(self.__dict__)


class Event(Model):
    pass


class Place(Model):
    pass


class Schedule(Model):
    pass
