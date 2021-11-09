import dockerEnv
import requests

def tfTest(img):
    files={"img":img}
    dockerEnv.activeEnv('tflite')
    response=requests.post('http://127.0.0.1:'+str(dockerEnv.ports['tflite'])+'/detect',files=files)
    print(response.text)
    return str(response.text)



