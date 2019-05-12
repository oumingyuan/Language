import xlrd


def get_data():
    data_head = ["month", "name", "base_pay", "push_money", "fine", "total_pay", "social_security", "accumulation_fund",
                 "individual_income_tax", "take_home_pay"]
    data = xlrd.open_workbook("C:\\Users\\oumin\\Desktop\\工资\\工资表.xls")

    table = data.sheets()[0]

    n_rows = table.nrows  # 行数

    n_cols = table.ncols  # 列数

    print("行数", n_rows)
    print("列数", n_cols)

    list = []

    for i in range(0, n_rows):
        map = {}
        rowValues = table.row_values(i)  # 某一行数据

        if i > 2:
            print(rowValues)

            # map["序号"] = rowValues[0]

            for j in range(len(data_head)):
                map[data_head[j]] = rowValues[j]
                # map["base_pay"] = rowValues[3]
                # map["take_home_pay"] = rowValues[16]

            list.append(map)
            # for item in rowValues:
            #     print(item)

    return list


print(get_data())
