# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: Image ocr demo.
"""
import time
import sys

sys.path.append('..')
from imgocr import ImgOcr

if __name__ == "__main__":
    m = ImgOcr(use_gpu=False)
    img_path = "data/hard1.jpg"
    s = time.time()
    result = m.ocr(img_path)
    e = time.time()
    print("total time: {:.4f} s".format(e - s))
    print("result:", result)
    for line in result:
        print(line['text'])

    print('-------------------\n')

    m = ImgOcr(use_gpu=False, is_efficiency_mode=False)
    s = time.time()
    result = m.ocr(img_path)
    e = time.time()
    print("total time: {:.4f} s".format(e - s))
    print("result:", result)
    for line in result:
        print(line['text'])
