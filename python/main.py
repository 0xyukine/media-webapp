from flask import Flask, render_template, jsonify, send_from_directory, send_file
import os

file_root ='/mnt/e/Stuff/'

app = Flask(__name__)

class DirObject:
    def __init__(self, obj, path):
        self.name = obj
        self.path = path
        self.fp_obj = os.path.join(path, obj)
        if os.path.isfile(self.fp_obj):
            self.type = "file"
            self.fp_obj = self.fp_obj
            print(self.fp_obj)
        elif os.path.isdir(self.fp_obj):
            self.type = "dir"
        else:
            self.type = "unkown"

@app.route('/')
def test():
    return render_template('index.html')

@app.route('/index')
def browse():
    item_list = []
    for item in os.listdir(file_root):
        item_list.append(DirObject(item, file_root))
    return render_template('root_index.html', item_list = item_list)

@app.route('/index/<path:path>', methods=['GET'])
def browser(path):
    print(path)
    item_list = []
    path = "/" + path
    for item in os.listdir(path):
        item_list.append(DirObject(item, path))
    return render_template('root_index.html', item_list = item_list)

@app.route('/file/<path:filepath>')
def get_file(filepath):
    filepath = "/" + filepath
    return send_file(filepath)

@app.route('/get_images', methods=['GET'])
def get_images():
    def get_exts(x):
        #split path and reverse elements in list
        return os.path.splitext(x)[::-1]

    dir_path = 'static/images/'

    #Create and sort list of files in directory
    files = []
    for item in os.listdir(dir_path):
        files.append(os.path.join(dir_path, item))
    files.sort(key=get_exts)

    return jsonify(files)

if __name__ == '__main__':
    app.run()