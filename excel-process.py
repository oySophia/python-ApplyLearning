#!/usr/bin/env python
#coding=utf-8

import xlrd
import xlwt
from datetime import date, datetime

def read_excel():
    file = xlwt.Workbook()
    table = file.add_sheet(u'sheet1',cell_overwrite_ok=True)
    workbook = xlrd.open_workbook('test.xls')  # 打开xls文件reading
    sheet1 = workbook.sheet_by_index(0)
    sheet2 = workbook.sheet_by_index(1)
    nrows2 = sheet2.nrows
    nrows1 = sheet1.nrows
    newrow = 0
    for i in range(0, nrows1):
        for j in range(0, nrows2):
            if sheet1.cell(i, 0).value == sheet2.cell(j, 1).value:
                table.write(newrow, 0, sheet2.cell(j, 0).value)
                table.write(newrow, 1, sheet1.cell(i, 0).value)
                table.write(newrow, 2, sheet1.cell(i, 1).value)
                table.write(newrow, 3, sheet1.cell(i, 2).value)
                table.write(newrow, 4, sheet1.cell(i, 3).value)
                table.write(newrow, 5, sheet1.cell(i, 4).value)
                table.write(newrow, 6, sheet1.cell(i, 5).value)
                table.write(newrow, 7, sheet1.cell(i, 6).value)
                table.write(newrow, 8, sheet1.cell(i, 7).value)
                table.write(newrow, 9, sheet1.cell(i, 8).value)
                table.write(newrow, 10, sheet2.cell(j, 1).value)
                table.write(newrow, 11, sheet2.cell(j, 2).value)
                table.write(newrow, 12, sheet2.cell(j, 3).value)
                table.write(newrow, 13, sheet2.cell(j, 4).value)
                table.write(newrow, 14, sheet2.cell(j, 5).value)
                table.write(newrow, 15, sheet2.cell(j, 6).value)
                table.write(newrow, 16, sheet2.cell(j, 7).value)
                print newrow
                newrow = newrow + 1
    file.save('result.xls')
    # 获取所有sheet
    print workbook.sheet_names()  # [u'sheet1', u'sheet2']
    sheet2_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(0)  # sheet索引从0开始
    #sheet2 = workbook.sheet_by_name('sheet2')

    # sheet的名称，行数，列数
    print sheet2.name, sheet2.nrows, sheet2.ncols

    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(0)  # 获取第三列内容
    print rows
    print cols

    # 获取单元格内容
    #print sheet2.cell(1, 0).value.encode('utf-8')
    #print sheet2.cell_value(1, 0).encode('utf-8')
    #print sheet2.row(1)[0].value.encode('utf-8')

    # 获取单元格内容的数据类型
    #print sheet2.cell(1, 0).ctype

def main():
    read_excel()

if __name__ == '__main__':
    main()