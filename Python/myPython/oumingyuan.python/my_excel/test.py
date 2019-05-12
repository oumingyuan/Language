#!/usr/bin/python
# coding=utf-8


import xlrd


book = xlrd.open_workbook("cat.xlsx")

sheet = book.sheet_by_name("Sheet1")

head_list = sheet.row_values(0)

data_list = sheet.row_values(1)

dictionary = {}

for i in range(0, sheet.ncols):
    dictionary[head_list[i]] = data_list[i]

print dictionary


