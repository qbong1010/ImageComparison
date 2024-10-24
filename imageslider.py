from flask import Flask, render_template, send_from_directory
import os
import glob

app = Flask(__name__)

@app.route('/')
def index():
    # before_after 디렉토리에서 *_before.png 파일들을 찾습니다
    before_files = glob.glob('before_after/*_before.png')
    # 파일 이름에서 * 부분만 추출 (경로와 _before.png 제거)
    image_names = [os.path.basename(f).replace('_before.png', '') for f in before_files]
    return render_template('imageslider.html', image_names=image_names)

@app.route('/before_after/<path:filename>')
def serve_image(filename):
    return send_from_directory('before_after', filename)

if __name__ == '__main__':
    app.run(debug=True)
