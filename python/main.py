from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html')

@app.route('/get_images', methods=['GET'])
def get_imageS():
    work_dir = os.path.dirname(os.path.realpath(__file__))
    #dir_path = os.path.join(work_dir,'static/images/')
    dir_path = 'static/images/'
    print(dir_path)
    files = []
    for file in os.listdir(dir_path):
        print(file)
        files.append(os.path.join(dir_path, file))
    return jsonify(files)

if __name__ == '__main__':
    app.run()