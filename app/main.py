import requests
import easyocr
import cv2

img_path = "images/pokemon_0.png"

img = cv2.imread(img_path)

reader = easyocr.Reader(['en'], gpu=True)

text = reader.readtext(img)

for t in text:
    print(t)

