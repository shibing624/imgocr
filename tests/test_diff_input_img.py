# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import sys
import unittest
import os

sys.path.append('..')
from imgocr.ppocr_onnx import ImgOcr

pwd_path = os.path.abspath(os.path.dirname(__file__))


class TestImgOcr(unittest.TestCase):

    def setUp(self):
        # Initialize the ImgOcr instance with default parameters
        self.m = ImgOcr()
        self.img_path = os.path.join(pwd_path, 'data/11.jpg')

    def test_ocr_img_path(self):
        result = self.m.ocr(self.img_path)
        print(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_ocr_img_pil(self):
        from PIL import Image
        img = Image.open(self.img_path)
        result = self.m.ocr(img)
        print(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_ocr_img_np(self):
        import cv2
        img = cv2.imread(self.img_path)
        result = self.m.ocr(img)
        print(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)


if __name__ == '__main__':
    unittest.main()
