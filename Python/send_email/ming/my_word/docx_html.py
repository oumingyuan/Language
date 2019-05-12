# 转换成html
from docx2html import convert
import HTMLParser

html_parser = HTMLParser.HTMLParser()
# 使用docx2html模块将docx文件转成html串，随后你想干嘛都行
html = convert("G:\\t.docx")

# 这句非常关键，docx2html模块将中文进行了转义，所以要将生成的字符串重新转义
print(html_parser.enescape(html))
