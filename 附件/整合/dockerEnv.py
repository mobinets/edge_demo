import docker
import requests
import time
dockerImageID={
    'tflite':'detect:v2'
}
dockerContainerID={
    'tflite':'tflite_container_v2'
}
ports={
    'tflite':5002
}
exPorts={
    'tflite':{'5002/tcp': 5002}
}
commands={
    'tflite':'python main.py'
}
workDir={
    'tflite':'/root/'
}

def activeEnv(platform):
    client = docker.from_env()
    try:
        con = client.containers.get(dockerContainerID[platform])
        if(con.status!='running'):
            print(con.status)
            con.restart()
            print(con.status)
            con = client.containers.get(dockerContainerID[platform])
            print(con.status)
            while con.status != 'running':
                print(con.status)
                con = client.containers.get(dockerContainerID[platform])
            print(con.status)
            time.sleep(3)
    except requests.exceptions.HTTPError:
        con = client.containers.run(image=dockerImageID[platform],
                                    working_dir=workDir[platform],
                                    command=commands[platform],
                                    name=dockerContainerID[platform],
                                    detach=True,
                                    ports=exPorts[platform]
                                    )
        while con.status != 'running':
            print(con.status)
            con = client.containers.get(dockerContainerID[platform])
            time.sleep(1)
    