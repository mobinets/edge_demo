此处是《边缘计算：原理、技术与实践》的系统实践代码仓库，请配合书中第12章的步骤展开实践。
## 系统目标
从0开始实现边缘计算系统，特别面向物联网场景的计算卸载过程。
### 自主实现定制化边缘服务器
* 物联网前端：发起计算请求、响应计算结果
* 边缘服务器端：运行服务、处理请求、返回计算结果
<div align="center">
<img width=40% src="https://mobinets.cn/edgebook/resources/luojijiagou.png"><br>逻辑架构图</img>
</div>

### 利用EdgeX快速搭建标准化边缘服务器
书中过程基于EdgeX官方文档实现，原版教程在<a href="https://docs.edgexfoundry.org/1.2/examples/LinuxTutorial/EdgeX-Foundry-tutorial-ver1.0.pdf">这里</a>。
中文实现过程请参考书中描述。

## 硬件使用
* 物联网前端设备：ESP32-Cam
* 显示屏：SSD1306
* 边缘服务器：树莓派3B+或4B（可以使用x86服务器，书中提到的依赖服务请按照相应的系统版本准备）
* 树莓派系统版本：RPI OS Buster

<div align="center">
<br><img width=20% src="https://mobinets.cn/edgebook/resources/esp32-cam.png"><br>ESP32-Cam</img>
<br><img width=20% src="https://mobinets.cn/edgebook/resources/ssd1306.png"><br>SSD-1306</img>
<br><img width=20% src="https://mobinets.cn/edgebook/resources/rpi.png"><br>树莓派</img>
</div>

## 代码说明
* Tensorflow提供的目标检测代码请使用<a href="https://github.com/tensorflow/examples/tree/9241dd1f44c503a95e540c85f5084e805bca6028/lite/examples/object_detection/raspberry_pi">9241dd1版本</a>。
* Docker镜像基础系统使用Python的Docker Hub官方镜像，版本：python:3.7-slim-buster
* 读者可考虑直接使用书中搭建好的<a href="https://hub.docker.com/r/csdotliu/detect">服务器端服务镜像</a>（版本使用v2）。
