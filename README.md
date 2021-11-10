此处是《边缘计算：原理、技术与实践》的系统实践代码仓库，请配合书中第12章的步骤展开实践。
## 系统目标
从0开始实现边缘计算系统，特别面向物联网场景的计算卸载过程。
### 自主实现定制化边缘服务器
<img width=40% src="https://mobinets.cn/edgebook/resources/luojijiagou.png">逻辑架构图</img>
<img width=40% src="https://mobinets.cn/edgebook/resources/esp32-cam.png">ESP32-Cam</img>
<img width=40% src="https://mobinets.cn/edgebook/resources/ssd1306.png">SSD-1306</img>
<img width=40% src="https://mobinets.cn/edgebook/resources/rpi.png">树莓派</img>
* 物联网前端：发起计算请求、响应计算结果
* 边缘服务器端：运行服务、处理请求、返回计算结果

### 利用EdgeX快速搭建标准化边缘服务器
书中过程基于EdgeX官方文档实现，逐步教程在<a href="">这里</a>。

## 硬件使用
* 物联网前端设备：ESP32-Cam
* 显示屏：SSD1306
* 边缘服务器：树莓派3B+或4B（可以使用x86服务器，书中提到的依赖服务请按照相应的系统版本准备）
* 树莓派系统版本：XXX

## 代码说明
* Tensorflow Lite请使用<a href="">XX版本</a>。
* 系统实现过程中使用的Docker image均指定了版本，请按照书中指定的版本拉取相应docker image。
* 读者可考虑直接使用书中搭建好的<a href="">服务器端服务镜像</a>。
