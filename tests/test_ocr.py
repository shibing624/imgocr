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

    def test_ocr_with_detection_and_recognition(self):
        result = self.m.ocr(self.img_path, det=True, rec=True)
        print(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_ocr_with_detection_only(self):
        result = self.m.ocr(self.img_path, det=True, rec=False)
        print(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_ocr_with_recognition_only(self):
        result = self.m.ocr(self.img_path, det=False, rec=True)
        print(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_ocr_with_invalid_image_path(self):
        img_path = 'invalid_path.jpg'
        with self.assertRaises(FileNotFoundError):
            self.m.ocr(img_path)


if __name__ == '__main__':
    unittest.main()
