from flask import Flask
from flask import request
from flask import render_template
import json 
import modules.functions

app = Flask(__name__,"/")

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/save-headers')
def save_headers():
    dict1 = {

        "cookies":{}
     }
    # print(request.headers)
    for i in request.headers:
        # print(i)  # 查看取出的 headers 資料
        dict1[i[0]]=i[1]

    for i in request.cookies:
        dict1['cookies'][i] = request.cookies[i]

    # print(request.cookies)

    file1 = open('./headers.json', 'w')
    file1.write(json.dumps(dict1))  # 存成 JSON
    return dict1

app.add_url_rule('/show-cookies', None, modules.functions.show_cookie)

@app.route("/basic-templates")
def basic_templates():
    return render_template("basic.html",name="sexy" ,age=25)

@app.route("/basic-templates2")
def basic_templates2():
    output={
        "name":"sexy lady",
        "age":37
    }
    return render_template("basic.html", **output)