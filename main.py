from PIL import Image
import pytesseract

FILENAME = './data/img.jpeg'
print(pytesseract.image_to_string(Image.open(FILENAME),config='digits'))
