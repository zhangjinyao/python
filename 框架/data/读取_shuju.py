import xlrd
def shuju():
    shuju=[]
    f=xlrd.open_workbook(r'C:\Users\zjy\PycharmProjects\untitled\框架\111\小.xls')     #打开excel表格
    sheet=f.sheets()[0]             #获取数据第一个标签
    num=sheet.nrows                 #获取文件有多少行
    for i in range(1,num):
        aaa=sheet.row_values(i)
        shuju.append(aaa)
    return shuju
shuju()

# def aa():
#     with open(r'..\driver\run.txt','r')as f:
#         aa=f.readlines()
#         return aa


