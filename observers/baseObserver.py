'''
Abstract base class for all observers.
'''
from abc import ABC

class BaseObserver(ABC):
    '''
    Abstract base class for all observers.
    '''
    def __init__(self):
        pass

    def notify(self, models, assets, liabilities, month):
        '''
        Update the observer with the given value.
        '''
        pass