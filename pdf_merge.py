# -*- coding:utf-8 -*-
# Author: Adam Mei
# Date: 2019-01-13
# Time: 17:35
# Name: pdf_merge.py
# ---------------------------------------------

# 目的是把一个文件夹当中所有的pdf文件合并起来变成一个文件
# 输出文件放在同一文件夹当中，名称为此文件夹的名字
# 输出文件需要有标签，分割合并之前的各个文件
# 文件合并时候的排序依靠文件名排序，如果文件自身上没有相关排序信息，需要手动先修改文件名。

# 首先通过一个程序来读取所有的文件名；
# 进行循环，依次把每一个文件中的每一页都写进输出文件

# 首先确认一下是否有现成的库可以使用。

import os
import os.path
import time

from PyPDF2 import PdfFileReader, PdfFileWriter

time1 = time.time()


# 使用os模块walk函数，搜索出某目录下的全部pdf文件
# 获取同一个文件夹下的所有PDF文件名

def getFileName(filepath):
    file_list = []
    for root_, dirs, files in os.walk(filepath):
        files.sort()
        for _ in files:
            if _[0] != ".":
                file_list.append(_)

    return file_list


# 合并同一个文件夹下所有PDF文件
def MergePDF(filepath, output_file_name):
    pdf_file_names = getFileName(filepath)
    # outfile = getFileName(filepath)[1] + '.pdf'
    outfile = output_file_name + '.pdf'

    root_dir = filepath

    output = PdfFileWriter()
    output_pages = 0

    for each in pdf_file_names:
        print(each)
        # 读取源pdf文件
        input = PdfFileReader(os.path.join(root_dir, each), "r")

        # 获得源pdf文件中页面总数
        pageCount = input.getNumPages()
        bookmark_pages = output_pages
        output_pages += pageCount
        print(pageCount)

        # 分别将page添加到输出output中
        for _ in range(0, pageCount):
            output.addPage(input.getPage(_))
        output.addBookmark(str(each), bookmark_pages, parent=None)

    print("All Pages Number:" + str(output_pages))

    # 最后写pdf文件
    outputStream = open(outfile, "wb")
    output.write(outputStream)
    outputStream.close()
    print("finished")


if __name__ == '__main__':
    pdf_file_path = "C:\\Users\\Downloads\\Documents"
    MergePDF(pdf_file_path, "abc")
