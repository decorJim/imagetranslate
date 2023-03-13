import cv2
import pytesseract
from langdetect import detect_langs

# Load the image
img = cv2.imread('comic_page.jpg')

# Preprocess the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Extract the text using pytesseract
text = pytesseract.image_to_string(gray, lang='eng')

# Detect the language(s) used in the text
langs = detect_langs(text)

# Determine if the text is in a foreign language
is_foreign = False
for lang in langs:
    if lang.lang != 'en' and lang.prob > 0.5:
        is_foreign = True
        break

if is_foreign:
    print("The image contains foreign language text.")
else:
    print("The image does not contain foreign language text.")
