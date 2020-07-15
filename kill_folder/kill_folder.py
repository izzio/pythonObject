# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 21:06
# @Author  : Seventy
# @Site    : 批量删除空白文件夹
# @File    : kill_folder.py
# @Software: PyCharm

import os


def del_emp_dir(path):
    for (root, dirs, files) in os.walk(path):
        for item in dirs:
            dir = os.path.join(root, item)
            try:
                os.rmdir(dir)
                print(dir)
            except Exception as e:
                print('Exception', e)


if __name__ == '__main__':
    # 需要删除空文件夹的路径
    dir = r'D:\Seventy\Music'
    del_emp_dir(dir)
