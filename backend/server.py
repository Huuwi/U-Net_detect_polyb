from flask import Flask, Response, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont ,ImageEnhance
from io import BytesIO
import os

def add_text_to_image(image, text, position, font_path=None, font_size=30):
    draw = ImageDraw.Draw(image)

    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()
    
    draw.text(position, text, font=font, fill="white")

i = 0
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app, resources={r"/handler_image": {"origins": "http://localhost:6969"}})

@app.route('/handler_image', methods=['POST'])
def handler_image():
    global i
    file = request.files["file"] 
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return jsonify({'error': 'File type not allowed'}), 400
    i += 1
    image = Image.open(BytesIO(file.read())) 

    '''
    
    dùng model ở đây
    
    
    '''


    text = "Hello, this is a test!"
    add_text_to_image(image, text, (150, 150), font_size=130)
    
    # Tạo đường dẫn lưu ảnh
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f'processed_{i}' + file.filename)
    
    # Lưu ảnh đã chỉnh sửa
    image.save(file_path)



    img_io = BytesIO()
    image.save(img_io, format='JPEG')
    img_io.seek(0)
    
    # Trả về ảnh đã chỉnh sửa
    return send_file(img_io, mimetype='image/jpeg', as_attachment=False, download_name='edited_image.jpg')

if __name__ == '__main__':
    app.run(debug=True)
