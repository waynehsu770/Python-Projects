


class Pet:

    def __init__(self):
        self.__privateVar = 'cat'
        self._protectedVar = 'turtle'

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Pet()
print(obj._protectedVar)
obj._protectedVar = 'bird'
print(obj._protectedVar)
obj.getPrivate()
obj.setPrivate('dog')
obj.getPrivate()
