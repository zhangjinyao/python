import xlrd
def shuju():
    shuju=[]
    f=xlrd.open_workbook(r'c:\Users\zjy\PycharmProjects\untitled\框架\111\注册测试.xls')     #打开excel表格
    sheet=f.sheets()[0]
    num=sheet.nrows
    for i in range(1,num):
        aaa=sheet.row_values(i)
        shuju.append(aaa)
    return shuju
shuju()
