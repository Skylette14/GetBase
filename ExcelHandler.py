import xlrd
import xlwt
import getreq

def readAndwriteExcel(filename):
	species_list = list()
	#读excel的表头
	data = xlrd.open_workbook(filename)
	table = data.sheet_by_name('Sheet3')
	#行数
	nrows = table.nrows
	#创建写表
	book = xlwt.Workbook(encoding = 'utf-8') #创建一个Excel对象
	sheet1 = book.add_sheet('sheet1') #添加一个名为sheet1的sheet
	style = xlwt.XFStyle()
	#读读表，写写表
	for i in range(1,101):
		species_list.append(table.cell(0,i).value.replace(" ",""))
		#写写表头
		sheet1.write(0,i,table.cell(0,i).value)
	for i in range(1, nrows):
		writeExcel(i, table.cell(i,0).value, species_list, sheet1)
		print(table.cell(i,0).value,"写入完成")
	#最后保存文档
	book.save("output.xls") # 保存

def writeExcel(rowNum, rowKey, species_list, sheet1):
	resultMap = getreq.get_result(rowKey)
	sheet1.write(rowNum, 0, rowKey)
	for i in range(len(species_list)):
		try:
			sheet1.write(rowNum, i+1, resultMap[species_list[i]])
		except:
			pass

def main():
	filename = "Full_100_name.xlsx"
	readAndwriteExcel(filename)


if __name__ == '__main__':
	main()
