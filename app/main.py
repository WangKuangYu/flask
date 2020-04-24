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

@app.route('/try-qs')
def queryString():
    # query string 轉成 dict
    # http://localhost:5000/try-qs?a[]=1&b=34&a[]=5
    output = {
        'args': request.args,
        'a[]': request.args.getlist('a[]'),
        'get_b': request.args.get('b'),
        'get_a[]': request.args.get('a[]'),
    }
    return output

@app.route('/try-post', methods=['POST'])  # 限定使用 POST
def try_post():
    # 表單資料 urlencoded, form-data 皆可, 使用 postman 測試
    return request.form

@app.route('/try-post2', methods=['POST'])
def try_post2():
    # 使用 postman post json 資料: {"a":11,"b":22}
    output = {
        'content_type': request.content_type,
        'data': request.data.decode('utf-8'),
        'json': request.get_json(),
    }
    return output

@app.route('/params/')
@app.route('/params/<action>/')
@app.route('/params/<action>/<int:id>')
def my_params(action='none', id=0):
    return ( {
        'action': action,
        'id': id
    } )