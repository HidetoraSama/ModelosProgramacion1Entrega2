import copy
from utilidades import pause

class Iclone:
    def shallowClone(self):
        return self

    def deepClone(self):
        return copy.deepcopy(self)


''' Director has a builder associated with him. Director the
delegates building of the smaller parts to the builder and
assembles them together.'''

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

    def set_body(self, body):
        self.__body = body

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def set_shield(self, shield):
        self.__shield = shield

    def stats(self):
        print ("Body shape: " + self.__body.shape)
        print ("Weapon damage per sec: " + str(self.__weapon.dmgps))
        print ("Shield protection per sec: " + str(self.__shield.protps))

'''Creates various parts of a character.
This class is responsible for constructing all
the parts for a character.'''

class Builder:

    def get_body(self):
        pass
    def get_weapon(self):
        pass
    def get_shield(self):
        pass

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

# Character parts
class Body(object):
    shape = None

class Weapon(object):
    dmgps = 0
    def show(self):
        pass
class Shield(object):
    protps = 0
    def show(self):
        pass

if __name__ =="__main__":

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
    
    pause()