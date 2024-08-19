from flask import Flask, render_template, request, redirect

import fileProcess
import settings

app = Flask(__name__)

iskey = False
Data = []

def haveKey():
    global  iskey
    iskey = fileProcess.FileProcess.haveKey()



@app.route('/')
def show():
    haveKey()
    if not iskey:
        return render_template('setting.html')
    else:
        return render_template('index.html')

@app.route("/start")
def start():
    haveKey()
    if not iskey:
        return render_template('setting.html')
    else:
        result = Data
        return render_template("start.html",result=result)

@app.route("/setting")
def setting():
    haveKey()
    return render_template("setting.html")

@app.route("/submit_API_KEY",methods=['post'])
def submitDone():
    haveKey()
    value = request.form.get("API_KEY")
    path = 'User Settings/config.txt'
    key = 'api_key'
    fileProcess.FileProcess().setKeyValue(path,new_key=key,new_value=value)
    return redirect("/")

def setKeyValueFile(self,value,key='api_key', path=None):
    haveKey()
    if path is None:
        path = self.path
    return fileProcess.FileProcess().setKeyValue(path,new_key=key,new_value=value)


@app.route("/Request_Show",methods=['post'])
def Request_Show():
    haveKey()
    global Data
    Data.append(request.form.get("Data"))


@app.route("/Request_Key",methods=['post'])
def Request_Key():
    key = 'api_key'
    path = 'User Settings/config.txt'
    result = fileProcess.FileProcess().getKeyValue(path,key)
    if result is not False:
        return result
    else:
        return 'False'


def run():
    app.run(port=2024,debug=True)



if __name__ == "__main__":
    app.run(port=2024,debug=True)
