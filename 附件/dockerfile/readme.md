## 借助dockerfile构建个性化镜像所需要的代码
```
.
├── code                        # docker镜像内所需代码
│   ├── annotation.py           # 标注代码
│   ├── detect_picamera.py      # 目标检测代码
│   ├── dog.jpg                 # 示例图片
│   ├── main.py                 # 简易web server
│   └── model                   # 目标检测模型及目标种类信息
│       ├── coco_labels.txt
│       ├── detect.tflite
│       └── mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite
├── dockerfile                  # 构建docker镜像所需的dockerfile文件
└── sources.list                # 替换到docker镜像中所需的源
```
