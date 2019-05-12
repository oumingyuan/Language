import xlwt
from ming.my_tool import read_excel

# month	name	base_pay	push_money	fine	total_pay	social_security	accumulation_fund	individual_income_tax	take_home_pay

data_head = ["month", "name", "base_pay", "push_money", "fine", "total_pay", "social_security", "accumulation_fund",
             "individual_income_tax", "take_home_pay"]
book = xlwt.Workbook()  # 创建excel对象
sheet = book.add_sheet('工资单')  # 添加一个表
# sheet.write(0, 1, 'Haha')  # 修改0行1列的数据为'Haha'

data_body = read_excel.get_data()

for i in range(len(data_head)):
    sheet.write(0, i, data_head[i])

for i in range(len(data_body)):
    data_map = data_body[i]

    print(data_map)

    for j in range(len(data_map)):
        print(j)
        sheet.write(1, j, data_map[data_head[j]])

book.save("C:\\Users\\oumin\\Desktop\\工资\\工资单.xls")
