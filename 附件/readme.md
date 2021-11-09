```
.
├── dockerfile              # 打包个性化docker镜像
│   ├── code
│   │   ├── annotation.py
│   │   ├── detect_picamera.py
│   │   ├── dog.jpg
│   │   ├── main.py
│   │   └── model
│   ├── dockerfile
│   └── sources.list
├── Esp32-Cam               # 前端物联网设备代码
│   └── esp32_test.ino
├── local                   # 本地部署测试代码
│   ├── detect_picamera.py
│   ├── dog.jpg
│   ├── main.py
│   └── model
└── 整合                    # 整合边缘服务器和前端物联网设备
    ├── annotation.py
    ├── app.py
    ├── dockerEnv.py
    ├── lables.py
    ├── methodCenter.py
    └── model
```