# -*- coding: utf-8 -*-

import pdftotext
from counter import count_words
import sys
file_name = sys.argv[1]
# Load your PDF
with open(file_name, "rb") as f:
    pdf = pdftotext.PDF(f)

# How many pages?
print("pages:",len(pdf))

res = u"\n\n".join(pdf)
# Read all the text into one string
print(count_words(res))

# 打开文件以写入模式（'w'表示写入，如果文件存在则清空，不存在则创建）
with open(file_name[:-4]+'.txt', 'w') as file:
    # 写入内容到文件
    file.write(res)
