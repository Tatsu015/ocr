from PIL import Image
import pyocr
import pytesseract
import cv2

# image = cv2.imread('./data/iraUG.jpeg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# data = pytesseract.image_to_string(gray, lang='eng', config='--psm 6').strip()
# print(data)
# print('--------------------------')

# num = pytesseract.image_to_string(Image.open('./data/img.jpeg'),config='digits').strip()
# print(num)
# print('--------------------------')

# longj = pytesseract.image_to_string(Image.open('./data/pyocr_test.png'),lang='jpn').strip()
# print(longj)
# print('--------------------------')


tools = pyocr.get_available_tools()
tool = tools[0]
jpn = tool.image_to_string(Image.open('./data/jpn_resize.png'),lang='jpn',builder=pyocr.builders.TextBuilder(tesseract_layout=3)).strip()

print(jpn)

