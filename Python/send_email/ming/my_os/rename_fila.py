#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 列出目录
print("目录为: %s" % os.listdir(os.getcwd()))

os.chdir("C:\\Users\\oumin\\Desktop\\snow")  # 将当前工作目录改变为`/Users/<username>/Desktop/`

print("目录为: %s" % os.listdir(os.getcwd()))

file_name_list = os.listdir(os.getcwd())

for file_name in file_name_list:
    os.rename(file_name, file_name[:-1])

# 重命名
# os.rename("test", "test2")

print("重命名成功。")

# 列出重命名后的目录
print("目录为: %s" % os.listdir(os.getcwd()))
