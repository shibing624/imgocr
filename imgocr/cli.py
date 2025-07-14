# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: Cli for image ocr.
"""
import argparse
import sys

import pandas as pd
from loguru import logger
from glob import glob
from tqdm import tqdm
import os

sys.path.append('..')
from imgocr.ppocr_onnx import ImgOcr


def save_partial_results(df, output_file, is_first_chunk):
    mode = 'w' if is_first_chunk else 'a'
    header = is_first_chunk
    file_dir = os.path.dirname(output_file)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    with open(output_file, mode, encoding='utf-8') as f:
        df.to_csv(f, index=False, header=header)


def parse_args():
    parser = argparse.ArgumentParser(description='imgocr cli')
    parser.add_argument('--image_dir', type=str, help='input image dir path, required', required=True)
    parser.add_argument('--output_dir', type=str, default='outputs', help='output ocr result dir path, default outputs')
    parser.add_argument('--chunk_size', type=int, default=50, help='chunk size, default 10')
    parser.add_argument('--use_gpu', type=bool, default=False, help='use gpu, default False')
    args = parser.parse_args()
    logger.debug(args)
    return args


def cli(args):
    m = ImgOcr(use_gpu=args.use_gpu, model_version='v5', is_efficiency_mode=True)
    images = glob(args.image_dir + '/*.[jJpP][pPnN][gG]')
    logger.info(f"Found {len(images)} images in {args.image_dir}")
    chunk_size = args.chunk_size
    for i in range(0, len(images), chunk_size):
        chunk_imgs = images[i:i + chunk_size]
        ocr_results = []
        for path in tqdm(chunk_imgs):
            try:
                res = m.ocr(path)
                res_list = [i['text'] for i in res if i]
                result = "\n".join(res_list)
                ocr_results.append(result)
            except Exception as e:
                logger.error(f'error: {e}, img: {path}')
                ocr_results.append("")
        # Save part result to dataframe
        chunk_df = pd.DataFrame({'images': chunk_imgs, 'ocr_results': ocr_results})
        output_file = os.path.join(args.output_dir, 'ocr_results.csv')
        save_partial_results(chunk_df, output_file, i == 0)
        logger.debug(f'saved partial results. size: {len(chunk_imgs)}, ocr_results size: {len(ocr_results)}')
    logger.info(f"Input image_dir {args.image_dir}, saved to {args.output_dir} success.")


def main():
    args = parse_args()
    cli(args)


if __name__ == "__main__":
    main()
