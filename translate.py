import pytesseract
from PIL import Image

# Set the path to the directory containing the trained data files
pytesseract.pytesseract.tesseract_cmd = r'tesseract'
tessdata_dir_config = r'--tessdata-dir "data\tessdata"'

# Load the image and extract the text
image = Image.open('image2.jpg')
text = pytesseract.image_to_string(image, lang='jpn', config=tessdata_dir_config)

# Print the extracted text
print(text)


