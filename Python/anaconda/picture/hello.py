# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image


class GetImageDate(object):
    @staticmethod
    def read():
        image = Image.open(u"\\Language\\Python\\anaconda\picture\\timg.jpg")
        text = pytesseract.image_to_string(image)
        return text

    def save_result_to_document(self):
        text = self.read()
        f = open(u"\\Language\\Python\\anaconda\\picture\\Verification.txt", "w")
        print(text)
        f.write(str(text))
        f.close()


g = GetImageDate()
g.save_result_to_document()
