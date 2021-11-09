from flask import Flask, request
import methodCenter
import lables
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/detect',methods=['POST'])
def tfDetect():
    data=request.data
    result=methodCenter.tfTest(data)
    if result:
        print(str(lables.lableInfo[int(float(result))]))
        return str(lables.lableInfo[int(float(result))])
    else:
        return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
