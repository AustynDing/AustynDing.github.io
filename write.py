# -*- coding: UTF-8 -*-

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os

# 遍历指定目录，显示目录下的所有文件名
import time


def eachFile(filepath):
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        with open(child, 'r+', encoding='utf-8') as f:
            old = f.read()
            f.seek(0)
            f.write('---\n')
            f.write('title: ' + allDir.split('.')[0] + '\n')
            f.write('date: ' + time.strftime("%Y-%m-%d %H:%M:%S") + '\n')
            f.write('categories: 计算机组成原理' + '\n')
            f.write('---\n')
            # title: page0
            # date: 2023 - 02 - 27
            # 19: 53:20
            # tags:
            f.write(old)
        # print(allDir.split('.'))
        # .decode('gbk')是解决中文显示乱码问题


# 读取文件内容并打印
def readFile(filename):
    fopen = open(filename, 'r')  # r 代表read
    for eachLine in fopen:
        print
        "读取到得内容如下：", eachLine
    fopen.close()


# 输入多行文字，写入指定文件并保存到指定文件夹
def writeFile(filename):
    fopen = open(filename, 'w')
    print
    "\r请任意输入多行文字", " ( 输入 .号回车保存)"
    while True:
        aLine = input()
        if aLine != ".":
            fopen.write('%s%s' % (aLine, os.linesep))
        else:
            print
            "文件已保存!"
            break
    fopen.close()


if __name__ == '__main__':
    filePath = "D:\\hexo\\source\\_posts"
    filePathI = "D:\\FileDemo\\Python\\pt.py"
    filePathC = "C:\\"
    eachFile(filePath)
    # readFile(filePath)
    # writeFile(filePathI)
