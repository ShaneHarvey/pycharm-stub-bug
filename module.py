

class MyClass(object):
    def __init__(self):
        self.__private_attr = []
        self.public_attr = []

    def __private_method(self):
        self.__private_attr.append(1)
        self.public_attr.append(1)

    def public_method(self):
        self.__private_method()
        self.__private_attr.append(2)
        self.public_attr.append(2)
        return self.public_attr
