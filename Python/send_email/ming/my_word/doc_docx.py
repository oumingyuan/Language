# python如何转换word格式、读取word内容、转成html？

import docx
from win32com import client as wc



print("begin")

# 首先将doc转换成docx
word = wc.Dispatch("Word.Application")

print(word)

doc = word.Documents.Open(r"C:\Users\oumin\Desktop\卓典食品香料（江苏）有限公司.doc")
# 使用参数16表示将doc转换成docx
doc.SaveAs(r"C:\Users\oumin\Desktop\卓典食品香料（江苏）有限公司.docx", 16)
doc.Close()

print("close")

word.Quit()

# 读取word内容
doc = docx.Document(r"C:\Users\oumin\Desktop\卓典食品香料（江苏）有限公司.docx")
data = doc.paragraphs[0].text
print(data)


