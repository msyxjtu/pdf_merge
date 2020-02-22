# -*- coding:utf-8 -*-
# Date: 2018-08-25
# Time: 09:14
# Name: pdf_rename.py
# ---------------------------------------------
import os

from pdfrw import PdfReader


def get_all_files_name(path):
    """输出一个列表，包括一个文件夹当中所有的没有被隐藏的文件名称。（用.前缀来判断是否隐藏）"""
    all_file = os.listdir(path)
    for _ in all_file:
        if _[0] == '.':
            all_file.remove(_)

    for _ in all_file:
        yield _


def rename_file_to_pdf_title(path, filename):
    full_file_name = os.path.join(path, filename)
    # print(full_file_name)
    # Extract pdf title from pdf file
    new_name = PdfReader(full_file_name).Info.Title
    # Remove surrounding brackets that some pdf titles have
    new_name = new_name.strip('()') + '.pdf'
    new_full_name = os.path.join(path, new_name)
    os.rename(full_file_name, new_full_name)


pdf_files_path = '/Users/adammei/Documents/Thesis'
all_pdf_files = get_all_files_name(pdf_files_path)
for _ in all_pdf_files:
    try:
        # print(_)
        full_name = os.path.join(pdf_files_path, _)
        if not os.path.isfile(full_name) or _[-4:] != '.pdf':
            continue
        # print(full_name)
        rename_file_to_pdf_title(pdf_files_path, _)
    except AttributeError:
        print(_, 'don"t have title')
