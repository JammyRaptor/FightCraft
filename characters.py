import nameGenerator as ng 

class baseCharacter:
    def __init__(self):
        self.type = 'Barbarian'
        self.health = 100
        self.power = 0
        self.sPower = 0
        self.speed = 0
        self.name = ng.generateName()
    
    def get_details(self):
        return {'type': self.type, 'name': self.name, 'power': self.power, 'special power': self.sPower, 'speed': self.speed, 'health': self.health}

class Barbarian(baseCharacter):
    def __init__(self):
        super().__init__()
        self.type = 'Barbarian'
        self.power = 70
        self.sPower = 20
        self.speed = 50

class Elf(baseCharacter):
    def __init__(self):
        super().__init__()
        self.type = 'Elf'
        self.power = 30
        self.sPower = 60
        self.speed = 10

class Wizard(baseCharacter):
    def __init__(self):
        super().__init__()
        self.type = 'Wizard'
        self.power = 50
        self.sPower = 70
        self.speed = 30

class Dragon(baseCharacter):
    def __init__(self):
        super().__init__()
        self.type = 'Dragon'
        self.power = 90
        self.sPower = 40
        self.speed = 50

class Knight(baseCharacter):
    def __init__(self):
        super().__init__()
        self.type = 'Knight'
        self.power = 60
        self.sPower = 10
        self.speed = 60
