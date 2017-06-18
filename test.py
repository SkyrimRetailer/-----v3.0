import os
import time

def findFile(path, pathlist):
    # 运用递归，寻找以.xlsx和.xls文件的path，并存储到pathlist列表中
    if os.path.isfile(path):
        if path.endswith('xlsx') or path.endswith('xls'):
            pathlist.append(path)
    else:
        files = os.listdir(path)
        for file in files:
            findFile(os.path.join(path, file), pathlist)
    return pathlist

pathlist = []
path = "请将需要统计的Excel文件放入该文件夹"
pathlist = findFile(path, pathlist)
if print(len(pathlist)) == 0:
    print("未找到Excel文件，请检查是文件否被放入正确的文件夹")
    print("=====程序将在5秒后关闭=====")
    time.sleep(5)
    exit(1)
else:
    print("找到如下文件：")
    for i in range(0, len(pathlist)):
        print("%d.%s" % (i+1, pathlist[i][len(path)+1:]))
while True:
    choice = int(input("请选择："))
    if choice in range(1, len(pathlist)):
        file = pathlist[choice-1]
        break
    else:
         print("输入有误，请输入1-%d" % (len(pathlist)))
