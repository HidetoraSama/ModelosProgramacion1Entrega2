from utilidades import pause

class Singleton(object):
    class __Singleton:
        def __init__(self):
            self.val = None
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)

if __name__ =="__main__":
    x = Singleton()
    x.val = 'sausage'
    print(x)
    print(id(x))
    
    y = Singleton()
    y.val = 'eggs'
    print(y)
    print(id(y))
    
    z = Singleton()
    z.val = 'spam'
    print(z)
    print(id(z))
    
    print(x)
    print(y)
    print(z)

    pause()