import xlrd
from message import Message
from container import Container

file = "2017年3月.xlsx"
#file = str(input("请输入文件名："))

excel = xlrd.open_workbook(file)
table = excel.sheet_by_name("个人")
container = Container()
nrows = table.nrows

for i in range(3, nrows):
    try:
        line = table.row_values(i)
        message = Message(line[1])
        message.setName(line[0])
        message.setTime(line[2])
        message.setBuilding(line[3])
        message.setRoom(str(line[4]))
        message.setAttribute(line[5])
        message.setMaterialType(1, line[6])
        message.setMaterialUnit(1, line[7])
        message.setMaterialNum(1, line[8])
        message.setMaterialType(2, line[9])
        message.setMaterialUnit(2, line[10])
        message.setMaterialNum(2, line[11])
        message.setMaterialType(3, line[12])
        message.setMaterialUnit(3, line[13])
        message.setMaterialNum(3, line[14])
        message.setMaterialType(4, line[15])
        message.setMaterialUnit(4, line[16])
        message.setMaterialNum(4, line[17])
        message.setMaterialType(5, line[18])
        message.setMaterialUnit(5, line[19])
        message.setMaterialNum(5, line[20])
        message.setMaterialType(6, line[21])
        message.setMaterialUnit(6, line[22])
        message.setMaterialNum(6, line[23])
        message.setMaterialType(7, line[24])
        message.setMaterialUnit(7, line[25])
        message.setMaterialNum(7, line[26])
        container.add(message)
    except(TypeError):
        print("excel中数据填写有误，请检查是否漏填材料数量")
while True:
    print("=======维修记录查询=======")
    print("1、按编号查询")
    print("2、按维修人员姓名查询")
    print("3、按宿舍楼查询")
    print("4、按寝室查询")
    print("5、按材料名查询")
    print("6、按属性查询")
    print("7、退出")
    choice = input("\n请选择：")
    if choice == '1':
        try:
            ID = str(input("请输入编号："))
            p = container.findByID(ID)
            p.show()
            print("---------查询完毕---------")
        except:
            print("---------查询完毕---------")

    if choice == '2':
        try:
            name = str(input("请输入姓名："))
            p = container.findByName(name)
            for i in p:
                i.show()
            print("---------查询完毕---------")
        except:
            print("---------查询完毕---------")

    if choice == '3':
        try:
            building = str(input("请输入楼名："))
            p = container.findByBuilding(building)
            for i in p:
                i.show()
            print("---------查询完毕---------")
        except:
            print("---------查询完毕---------")

    if choice == '4':
        try:
            building = str(input("请输入具体楼名："))
            room = str(input("请输入房间号："))
            p = container.findByRoom(building, room)
            for i in p:
                i.show()
            print("---------查询完毕---------")
        except:
            print("---------查询完毕---------")

    if choice == '5':
        try:
            material = str(input("请输入材料名："))
            p = container.findByMaterial(material)
            for i in p:
                i.show()
            print("---------查询完毕---------")
        except:
            print("---------查询完毕---------")

    if choice == '6':
        try:
            attribute = str(input("请输入属性："))
            p = container.findByAttribute(attribute)
            for i in p:
                i.show()
            print("---------查询完毕---------")
        except:
            print("---------查询完毕---------")

    if choice == '7':
        exit(1)



