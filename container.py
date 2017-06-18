import time
class Container():
    def __init__(self):
        self.messages = []

    def add(self, message):
        self.messages.append(message)

    def getAll(self):
        return self.messages[:]

    def findByName(self, Name):
        result = []
        for p in self.messages:
            if Name in p.getName():
                result.append(p)
        return result

    def findByID(self, ID):
        for p in self.messages:
            if ID == p.getID():
                return p
                break
        else:
            print('\n未找到该条信息\n')

    def getMaterialSumA(self, material):
        result = 0
        for p in self.messages:
            try:
                 for i in range(1,8):
                     if material == p.getMaterialType(i):
                            result += p.getMaterialNum(i)
            except(TypeError):
                ID = p.getID()
                print("错误单号：", ID)
                print("材料数值有误，请确认是否漏填或错填材料数量\n"
                      "数量栏的单元格格式为 常规 ，不能为文本型，否则会报错")
                print("=====程序将在5秒后关闭=====")
                time.sleep(5)
                exit(1)
        return result


    def getMaterialSumB(self, name, material):
        result = 0
        for p in self.messages:
            if name == p.getName():
                for i in range(1,8):
                    if material == p.getMaterialType(i):
                        result += p.getMaterialNum(i)
        return result

    def findByTimeA(self, Time):
        result = []
        for p in self.messages:
            if Time in p.getTime():
                result.append(p)
        return result

    def findByTimeB(self, name, Time):
        result = []
        for p in self.messages:
            if name == p.getName():
                if Time in p.getTime():
                    result.append(p)
        return result

    def findByRoom(self, buliding, room):
        result = []
        for p in self.messages:
            if buliding == p.getBuilding():
                if room in p.getRoom():
                    result.append(p)
        return result

    def findByAttribute(self, attribute):
        result = []
        for p in self.messages:
            if attribute == p.getAttribute():
                result.append(p)
        return result

    def findByMaterial(self, material):
        result = []
        for p in self.messages:
            for i in range(1, 8):
                if material in p.getMaterialType(i):
                    result.append(p)
        return result

    def findByBuilding(self, building):
        result = []
        for p in self.messages:
            if building in p.getBuilding():
                result.append(p)
        return result

    def getWorkSumA(self, work):
        result = 0
        for p in self.messages:
            if work in p.getAttribute():
                result += 1
        return result

    def getWorkSumB(self, name, work):
        result = 0
        for p in self.messages:
            if name == p.getName():
                if work in p.getAttribute():
                    result += 1
        return result
