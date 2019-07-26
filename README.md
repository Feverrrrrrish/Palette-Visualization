# Palette-Visualization
将各类图片（绘画、摄影等）的配色方应运用到数据可视化中 现支持R语言

## Requirements
* Python3.6
* haishoku
* Pillow
* tkinter

## Usage
准备好Python3以上版本，并下载好所需要的三个库，tkinter应该是内置好了的。之后，下载本文件，替换在haishoku库中的两个脚本（haishoku.py和haillow.py），打开palette.py，根据自己配色原图的保存位置修改第7行（fp = '/demo/01.jpg'）中的保存路径，运行后会看到两处的配色方案，第二处的配色方案去除了过于淡的配色，从而更好地应用于可视化，复制GUI界面中的16进制颜色方案的内容，在R中运行即可。

## Video
https://www.bilibili.com/video/av59501216
