# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from imgocr import ImgOcr, draw_ocr_boxes
import os
from glob import glob
from tqdm import tqdm
import pandas as pd

if __name__ == '__main__':
    m = ImgOcr(use_gpu=False, is_efficiency_mode=False)
    image_dir = 'data'
    saved_dir = 'ocr_results'
    if not os.path.exists(saved_dir):
        os.makedirs(saved_dir)
    images = glob(image_dir + '/*.[jJpP][pPnN][gG]')
    print(f"Found {len(images)} images in {image_dir}")
    ocr_results = []
    for path in tqdm(images):
        res = m.ocr(path)
        res_list = [i['text'] for i in res if i]
        result = "\n".join(res_list)
        ocr_results.append(result)
        # Save ocr box img
        saved_img_path = os.path.join(saved_dir, os.path.basename(path))
        draw_ocr_boxes(path, res, saved_img_path)
    df = pd.DataFrame({'images': images, 'ocr_results': ocr_results})
    output_file = os.path.join(saved_dir, 'ocr_results.csv')
    df.to_csv(output_file, index=False)
    print(f"OCR results saved to {output_file}")
