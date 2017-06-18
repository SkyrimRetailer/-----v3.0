class Message():
    def __init__(self, ID):
        self.id = ID
        self.name = None
        self.time = None
        self.building = None
        self.room = None
        self.attribute = None
        self.materialType1 = None
        self.materialUnit1 = None
        self.materialNum1 = None
        self.materialType2 = None
        self.materialUnit2 = None
        self.materialNum2 = None
        self.materialType3 = None
        self.materialUnit3 = None
        self.materialNum3 = None
        self.materialType4 = None
        self.materialUnit4 = None
        self.materialNum4 = None
        self.materialType5 = None
        self.materialUnit5 = None
        self.materialNum5 = None
        self.materialType6 = None
        self.materialUnit6 = None
        self.materialNum6 = None
        self.materialType7 = None
        self.materialUnit7 = None
        self.materialNum7 = None

    def setName(self, Name):
        self.name = Name
    def getName(self):
        return self.name

    def setID(self, ID):
        self.id = ID
    def getID(self):
        return self.id

    def setTime(self, Time):
        self.time = Time
    def getTime(self):
        return self.time

    def setBuilding(self, Building):
        self.building = Building
    def getBuilding(self):
        return self.building

    def setRoom(self, Room):
        self.room = Room
    def getRoom(self):
        return self.room

    def setAttribute(self, Attribute):
        self.attribute = Attribute
    def getAttribute(self):
        return self.attribute

    def setMaterialType(self, num, Type):
        if num == 1:
            self.materialType1 = Type
        if num == 2:
            self.materialType2 = Type
        if num == 3:
            self.materialType3 = Type
        if num == 4:
            self.materialType4 = Type
        if num == 5:
            self.materialType5 = Type
        if num == 6:
            self.materialType6 = Type
        if num == 7:
            self.materialType7 = Type

    def getMaterialType(self, num):
        if num == 1:
            return self.materialType1
        if num == 2:
            return self.materialType2
        if num == 3:
            return self.materialType3
        if num == 4:
            return self.materialType4
        if num == 5:
            return self.materialType5
        if num == 6:
            return self.materialType6
        if num == 7:
            return self.materialType7

    def setMaterialUnit(self, num, Unit):
        if num == 1:
            self.materialUnit1 = Unit
        if num == 2:
            self.materialUnit2 = Unit
        if num == 3:
            self.materialUnit3 = Unit
        if num == 4:
            self.materialUnit4 = Unit
        if num == 5:
            self.materialUnit5 = Unit
        if num == 6:
            self.materialUnit6 = Unit
        if num == 7:
            self.materialUnit7 = Unit

    def getMaterialUnit(self, num):
        if num == 1:
            return self.materialUnit1
        if num == 2:
            return self.materialUnit2
        if num == 3:
            return self.materialUnit3
        if num == 4:
            return self.materialUnit4
        if num == 5:
            return self.materialUnit5
        if num == 6:
            return self.materialUnit6
        if num == 7:
            return self.materialUnit7

    def setMaterialNum(self, num, Num):
        if num == 1:
            self.materialNum1 = Num
        if num == 2:
            self.materialNum2 = Num
        if num == 3:
            self.materialNum3 = Num
        if num == 4:
            self.materialNum4 = Num
        if num == 5:
            self.materialNum5 = Num
        if num == 6:
            self.materialNum6 = Num
        if num == 7:
            self.materialNum7 = Num

    def getMaterialNum(self, num):
        if num == 1:
            return self.materialNum1
        if num == 2:
            return self.materialNum2
        if num == 3:
            return self.materialNum3
        if num == 4:
            return self.materialNum4
        if num == 5:
            return self.materialNum5
        if num == 6:
            return self.materialNum6
        if num == 7:
            return self.materialNum7



    def show(self):
        print(str(self.getID()), str(self.getName()), str(self.getTime()), \
              str(self.getBuilding()), str(self.getRoom()), str(self.getAttribute()),\

            str(self.getMaterialType(1)), str(self.getMaterialUnit(1)), str(self.getMaterialNum(1)), \
            str(self.getMaterialType(2)), str(self.getMaterialUnit(2)), str(self.getMaterialNum(2)), \
            str(self.getMaterialType(3)), str(self.getMaterialUnit(3)), str(self.getMaterialNum(3)), \
            str(self.getMaterialType(4)), str(self.getMaterialUnit(4)), str(self.getMaterialNum(4)), \
            str(self.getMaterialType(5)), str(self.getMaterialUnit(5)), str(self.getMaterialNum(5)), \
            str(self.getMaterialType(6)), str(self.getMaterialUnit(6)), str(self.getMaterialNum(6)), \
            str(self.getMaterialType(7)), str(self.getMaterialUnit(7)), str(self.getMaterialNum(7)))