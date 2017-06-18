import xlrd
from xlwt import easyxf
from xlutils.copy import copy
import os
from container import Container
from message import Message
import time

#将此项目上传至GitHub

def findFile(path, pathlist):
    # 运用递归，寻找以.xlsx和.xls文件的path，并存储到pathlist列表中
    if os.path.isfile(path):
        if path.endswith('.xlsx') or path.endswith('.xls'):
            pathlist.append(path)
    else:
        files = os.listdir(path)
        for file in files:
            findFile(os.path.join(path, file), pathlist)
    return pathlist

print("\n欢迎使用维修部一键统计工具\n"
       "联系作者：蔡天扬 17725124327 292538095@qq.com\n")
#
# while True:
#     password = input("请输入密码：")
#     if password == "SkYoung":
#         print("密码正确")
#         break
#     else:
#         print("密码错误，请联系作者")

pathlist = []
path = "请将需要统计的Excel文件放入该文件夹"
pathlist = findFile(path, pathlist)
if len(pathlist) == 0:
    print("未找到Excel文件，请检查是文件否被放入正确的文件夹")
    print("=====程序将在5秒后关闭=====")
    time.sleep(5)
    exit(1)
else:
    print("找到如下文件：")#该部分代码为寻找文件夹内的excel文件以供选择
    for i in range(0, len(pathlist)):
        print("%d.%s" % (i+1, pathlist[i][len(path)+1:]))
while True:
    choice = int(input("请选择："))
    if choice in range(1, len(pathlist)+1):
        file = pathlist[choice-1]
        break
    else:
         print("输入有误，请输入1-%d" % (len(pathlist)))


rb = xlrd.open_workbook(file)

all = rb.sheet_by_name("个人")
container = Container()
allrows = all.nrows


for i in range(3, allrows):
    try:
        line = all.row_values(i)
        message = Message(str(line[1]))
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
    except(TypeError,):
        print("excel中数据填写有误，请检查是否漏填或错填材料数量\n"
              "注意材料数量那一栏的单元格格式为 常规，若是 文本型则会报错")
#读取总表中的信息,将每条信息创建成一个对象

wb = copy(rb)

#统计水材料
Wwater = wb.get_sheet(1)#写入
Rwater = rb.sheet_by_index(1)#读取
waterrows = Rwater.nrows
whead = Rwater.row_values(1)#表头数据
wlen = len(whead)
for i in range(2, waterrows):
    line = Rwater.row_values(i)
    sum1 = container.getMaterialSumA(line[1])
    Wwater.write(i, 3, sum1)#写入周总用量

    for j in range(4, wlen):
        sum2 = container.getMaterialSumB(whead[j], line[1])
        Wwater.write(i, j, sum2)#分别写入每人用量

#统计电材料
Welectric = wb.get_sheet(2)#写入
Relectric = rb.sheet_by_index(2)#读取
electricrows = Relectric.nrows
ehead = Relectric.row_values(1)#表头数据
elen = len(whead)
for i in range(2, electricrows):
    line = Relectric.row_values(i)
    sum1 = container.getMaterialSumA(line[1])
    Welectric.write(i, 3, sum1)#写入周总用量

    for j in range(4, elen):
        sum2 = container.getMaterialSumB(ehead[j], line[1])
        Welectric.write(i, j, sum2)#分别写入每人用量

#统计工具材料
Wtool = wb.get_sheet(3)#写入
Rtool = rb.sheet_by_index(3)#读取
toolrows = Rtool.nrows
thead = Rtool.row_values(1)#表头数据
tlen = len(thead)
for i in range(2, toolrows):
    line = Rtool.row_values(i)
    sum1 = container.getMaterialSumA(line[1])
    Wtool.write(i, 3, sum1)#写入周总用量

    for j in range(4, tlen):
        sum2 = container.getMaterialSumB(thead[j], line[1])
        Wtool.write(i, j, sum2)#分别写入每人用量

#统计工作量
Wcount = wb.get_sheet(4)#写入
Rcount = rb.sheet_by_index(4)#读取
countrows = Rcount.nrows
chead = Rcount.row_values(1)#表头数据
clen = len(chead)
for i in range(2, countrows):
    line = Rcount.row_values(i)
    sum1 = container.getWorkSumA(line[0])
    Wcount.write(i, 1, sum1)#写入周总工作量

    for j in range(2, clen):
        sum2 = container.getWorkSumB(chead[j], line[0])
        Wcount.write(i, j, sum2)#写入i行j列每人工作量

wb.save("统计结果.xls")
print("=========操作成功==========")
print("=====程序将在5秒后关闭=====")
time.sleep(5)
