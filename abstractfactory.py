from utilidades import pause

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
        return WeaponSwordsman();
    def get_shield(self):
        return ShieldSwordsman();

class SorcererFactory(object):
    def get_weapon(self):
        return WeaponSorcerer();
    def get_shield(self):
        return ShieldSorcerer();
    
class KnightFactory(object):
    def get_weapon(self):
        return WeaponKnight();
    def get_shield(self):
        return ShieldKnight();
    
# Product Interface
class Weapon(object):
    def show(self):
        pass
class Shield(object):
    def show(self):
        pass      
        
# Products
# Weapons
class WeaponSwordsman(object):
    def show(self):
        return 'Showing sharp sword'
class WeaponSorcerer(object):
    def show(self):
        return 'Showing two-handed staff'
class WeaponKnight(object):
    def show(self):
        return 'Showing heavy sword'

# Shields
class ShieldSwordsman(object):
    def show(self):
        return 'Showing tiny shield'
class ShieldSorcerer(object):
    def show(self):
        return 'Showing round shield'
class ShieldKnight(object):
    def show(self):
        return 'Showing heavy shield'

    
    
if __name__ =="__main__":
    factory = StandardFactory.get_factory('swordsman')
    weapon = factory.get_weapon()
    shield = factory.get_shield()
    print (weapon.show())
    print (shield.show())
   
    factory = StandardFactory.get_factory('sorcerer')
    weapon = factory.get_weapon()
    shield = factory.get_shield()
    print (weapon.show())
    print (shield.show())

    factory = StandardFactory.get_factory('knight')
    weapon = factory.get_weapon()
    shield = factory.get_shield()
    print (weapon.show())
    print (shield.show())

    pause()