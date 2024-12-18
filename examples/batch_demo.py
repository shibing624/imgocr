# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from imgocr.cli import cli
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='imgocr cli')
    parser.add_argument('--image_dir', type=str, help='input image dir path, required', default='data')
    parser.add_argument('--output_dir', type=str, default='ocr_results', help='output ocr result dir path, default outputs')
    parser.add_argument('--chunk_size', type=int, default=50, help='chunk size, default 10')
    parser.add_argument('--use_gpu', type=bool, default=False, help='use gpu, default False')
    args = parser.parse_args()
    print(args)
    cli(args)
