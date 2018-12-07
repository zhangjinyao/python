import xlrd
def bb():
    shuju = []
    f = xlrd.open_workbook(r'c:\Users\zjy\PycharmProjects\untitled\外部测试\data\qq.xls')
    sheet=f.sheets()[0]
    num = sheet.nrows
    for i in range(1,num):
        aaa = sheet.row_values(i)
        shuju.append(aaa)
    return shuju

