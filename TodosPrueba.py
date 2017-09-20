import copy
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

class Iclone:
    def shallowClone(self):
        return self

    def deepClone(self):
        return copy.deepcopy(self)

#Abstract Factory
class StandardFactory(object):
    
    @staticmethod
    def get_factory(factory):
        if factory == 'swordsman':
            return SwordsmanFactory()
        elif factory == 'sorcerer':
            return SorcererFactory()
        elif factory == 'knight':
            return KnightFactory()
        raise TypeError('Unknown Factory')

#Factory
class SwordsmanFactory(object):
    def get_weapon(self):
        return WeaponSwordsman()
    def get_shield(self):
        return ShieldSwordsman()
    def get_body(self):
        return BodySwordsman()

class SorcererFactory(object):
    def get_weapon(self):
        return WeaponSorcerer()
    def get_shield(self):
        return ShieldSorcerer()
    def get_body(self):
        return BodySorcerer()
    
class KnightFactory(object):
    def get_weapon(self):
        return WeaponKnight()
    def get_shield(self):
        return ShieldKnight()
    def get_body(self):
        return BodyKnight()
    
# Product Interface
class Weapon(object):
    dmgps = 0
    def show(self):
        pass
class Shield(object):
    protps = 0
    def show(self):
        pass
class Body(object):
    shape = ""
    def show(self):
        pass     
        
# Family Products
# Weapons (Family A)
# Product A1
class WeaponSwordsman(object):
    dmgps = 100
    def show(self):
        return 'swordsman-weapon'
# Product A2
class WeaponSorcerer(object):
    dmgps = 70
    def show(self):
        return 'sorcerer-weapon'
# Product A3
class WeaponKnight(object):
    dmgps = 50
    def show(self):
        return 'knight-weapon'

# Shields (Family B)
# Product B1
class ShieldSwordsman(object):
    protps = 20
    def show(self):
        return 'swordsman-shield'
# Product B2
class ShieldSorcerer(object):
    protps = 50
    def show(self):
        return 'sorcerer-shield'
# Product B3
class ShieldKnight(object):
    protps = 70
    def show(self):
        return 'knight-shield'

# Bodies (Family C)
# Product C1
class BodySwordsman(object):
    shape = "swordsman-body"
    def show(self):
        return 'swordsman-body'
# Product C2
class BodySorcerer(object):
    shape = "sorcerer-body"
    def show(self):
        return 'sorcerer-body'
# Product C3
class BodyKnight(object):
    shape = "knight-body"
    def show(self):
        return 'knight-body'

class Director:

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # The algorithm for assembling a character
    def getCharacter(self):
        character = Character()

        # First goes the body
        body = self.__builder.get_body()
        character.set_body(body)
        # Then weapon
        weapon = self.__builder.get_weapon()
        character.set_weapon(weapon)
        # Then shield
        shield = self.__builder.get_shield()
        character.set_shield(shield)

        return character

# The whole product

'''A character is assembled by the Director class from
parts made by Builder. Both these classes have
influence on the resulting object.'''

class Character(Iclone):

    def __init__(self):
        self.__body = None
        self.__weapon  = None
        self.__shield  = None
        self.health = 100

    def set_body(self, body):
        self.__body = body

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def set_shield(self, shield):
        self.__shield = shield

    def stats(self):
        return self.health, self.__weapon.dmgps, self.__shield.protps
'''        print ("Health points: " + str(self.health))
        print ("Body shape: " + self.__body.shape)
        print ("Weapon damage per sec: " + str(self.__weapon.dmgps))
        print ("Shield protection per sec: " + str(self.__shield.protps))'''

'''Creates various parts of a character.
This class is responsible for constructing all
the parts for a character.'''

class Builder:

    def get_body(self): pass
    def get_weapon(self): pass
    def get_shield(self): pass

'''Concrete Builder implementation.
This class builds parts for Swordsmans.'''

class SwordsmanBuilder(Builder):

    def get_body(self):
        body = Body()
        body.shape = "swordsman-body"
        return body

    def get_weapon(self):
        weapon = Weapon()
        weapon.dmgps = 100 #Algo para sacarlo del otro lado
        return weapon

    def get_shield(self):
        shield = Shield()
        shield.protps = 20 #Algo para sacarlo del otro lado
        return shield

'''Concrete Builder implementation.
This class builds parts for Sorcerers.'''

class SorcererBuilder(Builder):

    def get_body(self):
        body = Body()
        body.shape = "sorcerer-body"
        return body

    def get_weapon(self):
        weapon = Weapon()
        weapon.dmgps = 70 #Algo para sacarlo del otro lado
        return weapon

    def get_shield(self):
        shield = Shield()
        shield.protps = 50 #Algo para sacarlo del otro lado
        return shield

'''Concrete Builder implementation.
This class builds parts for Knights.'''

class KnightBuilder(Builder):

    def get_body(self):
        body = Body()
        body.shape = "knight-body"
        return body

    def get_weapon(self):
        weapon = Weapon()
        weapon.dmgps = 50 #Algo para sacarlo del otro lado
        return weapon

    def get_shield(self):
        shield = Shield()
        shield.protps = 70 #Algo para sacarlo del otro lado
        return shield

'''if __name__ =="__main__":

    x = Singleton()
    x.val = StandardFactory.get_factory('sorcerer')
    weapon = x.val.get_weapon()
    shield = x.val.get_shield()
    body = x.val.get_body()
    print(repr(x))
    print((id(x)))
    print (weapon.show())
    print (shield.show())
    print (body.show())

    y = Singleton()
    y.val = StandardFactory.get_factory('knight')
    weapon = y.val.get_weapon()
    shield = y.val.get_shield()
    print(repr(y))
    print((id(y)))
    print (weapon.show())
    print (shield.show())

    print(repr(x))
    print((id(x)))
    print (weapon.show())
    print (shield.show())
    
    print("--=--" * 15)
    print(str(weapon.dmgps))
    print(str(shield.protps))

    print ("******" * 18)

    swordsmanBuilder = SwordsmanBuilder()
    sorcererBuilder = SorcererBuilder()
    knightBuilder = KnightBuilder()

    director = Director()

    # Build Swordsman
    print ("Swordsman")
    director.setBuilder(swordsmanBuilder)
    swordsman = director.getCharacter()
    swordsman.stats()

    print ("")

    # Build Sorcerer
    print ("Sorcerer")
    director.setBuilder(sorcererBuilder)
    sorcerer = director.getCharacter()
    sorcerer.stats()

    print ("")

    # Build knight
    print ("Knight")
    director.setBuilder(knightBuilder)
    knight = director.getCharacter()
    knight.stats()

    print ("--=--" * 15)

    supershield = Shield()
    supershield.protps = 1000

    kni2 = knight.deepClone()
    kni3 = kni2.shallowClone()
    
    kni3.set_shield(supershield)

    knight.stats()
    kni2.stats()
    kni3.stats()

    pause()'''