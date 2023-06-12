from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html')

@app.route('/browser')
def browse():
    return "<h1>lul</h1>"

@app.route('/get_images', methods=['GET'])
def get_imageS():
    def get_exts(x):
        #split path and reverse elements in list
        return os.path.splitext(x)[::-1]

    work_dir = os.path.dirname(os.path.realpath(__file__))
    #dir_path = os.path.join(work_dir,'static/images/')
    dir_path = 'static/images/'
    print(dir_path)
    files = os.listdir(dir_path)
    files.sort(key = get_exts)

    for x in range(len(files)):
        # files.append(os.path.join(dir_path, file))
        files[x] = os.path.join(dir_path,files[x]) 

    print(files)
    return jsonify(files)

if __name__ == '__main__':
    app.run()