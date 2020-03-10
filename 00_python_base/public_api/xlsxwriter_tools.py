# -*- coding:utf8 -*-
"""
Created on:
@author: BoobooWei
Email: rgweiyaping@hotmail.com
Version: V.19.03.09.0
Description: 常用的表格操作方法
Help:
"""

# 3rd-part Modules
import xlsxwriter


class CreateMyExcel:
    """
    创建excel表格
    """

    def __init__(self, excel):
        # Create an new Excel file.
        self.workbook = xlsxwriter.Workbook(excel)

    def create_new_sheet(self):
        # add a worksheet.
        worksheet = self.workbook.add_worksheet()
        return worksheet

    def insert_data(self, worksheet, title, lines):
        # insert title
        for i in range(len(title)):
            # 第一1行，每个列分别写入指定的数据
            worksheet.write(0, i, title[i])
        # insert row
        row = 1
        for line in lines:
            for column in range(len(line)):
                worksheet.write(row, column, line[column])
            row = row + 1

    def close_excel(self):
        self.workbook.close()


if __name__ == "__main__":
    # 创建excel表格并写入三个sheet
    api = CreateMyExcel('1.xlsx')
    title = ['编号', '标题', '所属客户']
    lines = [[1, 'a', '1'], [2, 'b', '2']]

    for i in range(3):
        api.insert_data(api.create_new_sheet(), title, lines)
    api.close_excel()

    # 将三个sheet合并成一个sheet
