# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import sys
import unittest
import os
import time

sys.path.append('..')
from imgocr.ppocr_onnx import ImgOcr

pwd_path = os.path.abspath(os.path.dirname(__file__))


class TestImgOcr(unittest.TestCase):

    def setUp(self):
        # Initialize the ImgOcr instance with default parameters
        self.m = ImgOcr()
        self.img_path = os.path.join(pwd_path, 'data/2.jpg')

    def test_ocr_with_detection_and_recognition(self):
        total_time = 0
        result = ''
        for _ in range(20):
            start_time = time.time()
            result = self.m.ocr(self.img_path, det=True, rec=True)
            end_time = time.time()
            total_time += (end_time - start_time)
            self.assertIsInstance(result, list)
            self.assertGreater(len(result), 0)
        avg_time = total_time / 20
        print(f"Average OCR with detection and recognition took {avg_time:.4f} seconds")
        print(result)

    def test_ocr_with_detection_only(self):
        total_time = 0
        result = ''
        for _ in range(20):
            start_time = time.time()
            result = self.m.ocr(self.img_path, det=True, rec=False)
            end_time = time.time()
            total_time += (end_time - start_time)
            self.assertIsInstance(result, list)
            self.assertGreater(len(result), 0)
        avg_time = total_time / 20
        print(f"Average OCR with detection only took {avg_time:.4f} seconds")
        print(result)

    def test_ocr_with_recognition_only(self):
        total_time = 0
        result = ''
        for _ in range(20):
            start_time = time.time()
            result = self.m.ocr(self.img_path, det=False, rec=True)
            end_time = time.time()
            total_time += (end_time - start_time)
            self.assertIsInstance(result, list)
            self.assertGreater(len(result), 0)
        avg_time = total_time / 20
        print(f"Average OCR with recognition only took {avg_time:.4f} seconds")
        print(result)


if __name__ == '__main__':
    unittest.main()
