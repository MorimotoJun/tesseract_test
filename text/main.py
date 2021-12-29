from pytesseract import pytesseract
from PIL import Image

img = Image.open('test.png')
pytesseract.tesseract_cmd = '/usr/bin/tesseract'
txt = pytesseract.image_to_string(img, lang='jpn')

f = open('output.txt', 'w', encoding='UTF-8')
f.write(txt)
f.close()