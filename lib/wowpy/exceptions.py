# -*- coding: utf-8 -*-

class WowpyBaseException(Exception):
    """ Base exception wraper """
    
class WowpyNetworkException(WowpyBaseException):
    """ All kind of connetctivity problems belong this exception """
    
    