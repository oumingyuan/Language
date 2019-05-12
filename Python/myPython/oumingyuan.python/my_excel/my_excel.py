#!/usr/bin/python
# coding=utf-8

import xlrd


# read the excel file into the computer memory
# author: oumingyuan

book = xlrd.open_workbook("excelFile.xlsx")


# put the information in dictionary list
# author: oumingyuan

sheet = book.sheet_by_name("报文数据")

head_list = sheet.row_values(0)

dictionary_list = []

for i in range(1, sheet.nrows):

    data_list = sheet.row_values(i)

    dictionary = {}

    for j in range(0, sheet.nrows):

        dictionary[head_list[j]] = data_list[j]

    dictionary_list.append(dictionary)

print dictionary_list
