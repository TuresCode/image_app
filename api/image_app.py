from flask import Flask, request, render_template
import pytesseract
from PIL import Image
from io import BytesIO


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return "No image found!"
    image_file = request.files['image']
    try:
    # Open the image
        image = Image.open(image_file)
    # Get the size of the image (width and height)
        width, height = image.size
    # Print the size
        extracted_text = pytesseract.image_to_string(image)
    except IOError:
        print("Unable to open the image.")
        extracted_text = 'Unable to open the image and extract text'

  
    # Perform OCR using Tesseract OCR
    extracted_text = f'excracted text coming soon'

    return extracted_text

#if __name__ == '__main__':
#    app.run(debug=True, port=5005, host='0.0.0.0')

