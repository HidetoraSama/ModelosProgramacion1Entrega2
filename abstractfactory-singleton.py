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
        return 'Showing sharp sword'
# Product A2
class WeaponSorcerer(object):
    dmgps = 70
    def show(self):
        return 'Showing two-handed staff'
# Product A3
class WeaponKnight(object):
    dmgps = 50
    def show(self):
        return 'Showing heavy sword'

# Shields (Family B)
# Product B1
class ShieldSwordsman(object):
    protps = 20
    def show(self):
        return 'Showing tiny shield'
# Product B2
class ShieldSorcerer(object):
    protps = 50
    def show(self):
        return 'Showing round shield'
# Product B3
class ShieldKnight(object):
    protps = 70
    def show(self):
        return 'Showing heavy shield'

# Bodies (Family C)
# Product C1
class BodySwordsman(object):
    shape = "swordsman-body"
    def show(self):
        return 'Showing skinny body'
# Product C2
class BodySorcerer(object):
    shape = "sorcerer-body"
    def show(self):
        return 'Showing delicate body'
# Product C3
class BodyKnight(object):
    shape = "knight-body"
    def show(self):
        return 'Showing strong body'

if __name__ =="__main__":
    x = Singleton()
    x.val = StandardFactory.get_factory('sorcerer')
    weapon = x.val.get_weapon()
    shield = x.val.get_shield()
    print(repr(x))
    print((id(x)))
    print (weapon.show())
    print (shield.show())

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

    pause()