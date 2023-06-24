from flask import Flask, render_template, jsonify, send_from_directory, send_file, request
import os

file_root ='/mnt/e/Stuff/'

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

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
        
        if obj.endswith(('jpg', 'jpeg', 'png')):
            self.media = "image"
        elif obj.endswith(('mp4', 'webm', 'ogg')):
            self.media = "video"
        else:
            self.media = "unknown"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

@app.route('/')
def index():
    return "<h1>Index coming soon™</h1>"

@app.route('/ls')
def ls():
    def get_exts(x):
        #split path and reverse elements in list
        return os.path.splitext(x)[::-1]

    #Create and sort list of files in directory
    dir_path = request.args.get('ls')
    if dir_path == "/":
        dir_path = file_root
    files = []
    for item in os.listdir(dir_path):
        files.append(os.path.join(dir_path, item))
    #files.sort(key=get_exts)

    files = [f for f in files if os.path.isfile(f)]

    return jsonify(files)

@app.route('/f/',defaults={'url_path':file_root})
@app.route('/f/<path:url_path>')
def browser(url_path):
    path = f"/{url_path}"
    print(url_path, path)
    if os.path.isfile(path):
        return send_file(path)
    elif os.path.isdir(path):
        dir_list = []

        print(os.listdir(path))

        for item in os.listdir(path):
            dir_list.append(DirObject(item, path))
            print(path, item)

        return render_template('ls.html', dir_list = dir_list)
    else:
        return "<h1>500</h1>"

if __name__ == '__main__':
    app.run()
