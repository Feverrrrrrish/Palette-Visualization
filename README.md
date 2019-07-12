# Palette-Visualization
将各类图片（绘画、摄影等）的配色方案运用到数据可视化中

## Requirements
* python3.6
* haishoku
* Pillow
* tkinter

## Usage
准备好Python3以上版本，并下载好所需要的三个库，tkinter应该是内置好了的。之后，下载本文件，替换在haishoku库中的两个脚本（haishoku.py和haillow.py），打开palette.py，并修改第7行（fp = '/demo/01.jpg'）中配色方案原图的保存路径，运行后会看到两处的配色方案，第二处的配色方案去除了过于淡的配色，从而更好地应用于可视化，复制GUI界面中的16进制颜色方案的内容，在R中运行即可。
