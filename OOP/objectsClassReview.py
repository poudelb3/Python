class NameOfClass():
    class_attribute = 'value'
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        pass

    #  the @classmethod && @staticmethod allows to call methods without 
    # instantiating any objects

    @staticmethod
    def stc_method(param1, param2):
        pass