# -*- coding: utf-8 -*-

# Build-in Modules
import os
import time
import shutil

# 3rd-part Modules
import xlsxwriter

now_date = time.strftime('%Y%m%d', time.localtime())


class OSHelper:
    def __init__(self):
        pass

    def mkdir(self, path):
        """
        在当前目录下创建子目录
        """
        try:
            os.makedirs(path)
        except Exception as e:
            print(str(e))
            return path
        else:
            return path

    def rmdir(self, path):
        """
        递归删除目录
        """
        try:
            shutil.rmtree(path)
        except Exception as e:
            print(str(e))
            return path
        else:
            return path

    def rmfile(self, path):
        """
        删除文件
        """
        try:
            os.remove(path)
        except Exception as e:
            print(str(e))
            return path
        else:
            return path


class ToExcel:
    def __init__(self, **kwargs):
        # 创建目录
        os_api = OSHelper()
        dir_name = os_api.mkdir(kwargs['dir_name'])
        self.file_name = os.path.join(dir_name, '{}-{}.xlsx'.format(kwargs['file_name'], now_date))
        self.workbook = xlsxwriter.Workbook(self.file_name)

    def write_file_column(self, work, worksheet, list_name):
        top = self.workbook.add_format(
            {'border': 1, 'align': 'center', 'bg_color': '#83CAF4', 'font_size': 10, 'bold': True})  # 设置单元格格式
        j = 0
        for i in list_name:
            worksheet.write(0, j, i, top)
            j += 1

    def add_sheet(self, shee_name, list_name, list_keys, lines):
        column = self.workbook.add_format({'border': 1, 'align': 'center', 'font_size': 10})
        worksheet = self.workbook.add_worksheet(shee_name)

        for _c in range(len(list_keys)):
            worksheet.set_column('{0}:{0}'.format(chr(_c + ord('A'))), 20)
        self.write_file_column(self, worksheet, list_name)
        row = 1
        for i in lines:
            for col in range(len(list_name)):
                worksheet.write(row, col, i.get(list_keys[col], 'no_result'), column)
            row = row + 1

    def write_close(self):
        self.workbook.close()


if __name__ == "__main__":
    params_excel = {
        'file_name': "测试表格名称",
        'dir_name': "测试目录地址",
    }
    excel_api = ToExcel(**params_excel)
    sheet_name = 'SLB列表'
    list_name = ['实例ID', '实例描述', '内网地址', '地域', '状态']
    list_keys = ['instance_id', 'instance_description', 'connection_address', 'region_id', 'tag']
    lines = [{'instance_id': 1, 'instance_description': 1, 'connection_address': 1, 'region_id': 1, 'tag': 1},
             {'instance_id': 1, 'instance_description': 1, 'connection_address': 1, 'region_id': 1, 'tag': 1},
             {'instance_id': 1, 'instance_description': 1, 'connection_address': 1, 'region_id': 1, 'tag': 1}]
    excel_api.add_sheet(sheet_name, list_name, list_keys, lines)
    excel_api.write_close()
