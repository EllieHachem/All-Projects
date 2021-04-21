class Animal:
    def __init__(self, speed, height, dmg, magic):
        self.speed = speed
        self.height = height
        self.dmg = dmg
        self.magic = magic 
        self.base_critical_chance = 4
        self.base_armour_penetration = 2

    def speed_increase(self):
        self.speed = 55            


    
