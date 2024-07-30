from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont 
from io import BytesIO
import os
app = Flask(__name__)


def add_text_to_image(image, text, position, font_path=None, font_size=30):
    draw = ImageDraw.Draw(image)

    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()
    
    draw.text(position, text, font=font, fill="white")

i = 0

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
        # Tạo đường dẫn lưu ảnh
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f'{i}' + file.filename)



    '''
    
    dùng model ở đây dùng model với biến image
    
    
    '''


    # text = "Hello, this is a test!" # test chinh sua
    # add_text_to_image(image, text, (150, 150), font_size=130)
    

    
    
    
    # Lưu ảnh đã chỉnh sửa vào folder uploads
    image.save(file_path)







    img_io = BytesIO()
    image.save(img_io, format='JPEG')
    img_io.seek(0)
    
    # Trả về ảnh đã chỉnh sửa
    return send_file(img_io, mimetype='image/jpeg', as_attachment=False, download_name='edited_image.jpg')

if __name__ == '__main__':
    app.run(debug=True)
