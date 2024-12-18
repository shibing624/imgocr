# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: pip install gradio
"""

import gradio as gr
from imgocr import ImgOcr

model = ImgOcr()


def get_text(img_path):
    ocr_result = model.ocr(img_path)[0]
    print("{} \t\t {}".format(img_path, ocr_result))
    ocr_text = [i[-1][0] for i in ocr_result]
    r = '\n'.join(ocr_text)
    print(r)
    return r


if __name__ == '__main__':
    examples = [
        ['data/1.jpg'],
        ['data/11.jpg'],
        ['data/12.jpg'],
        ['data/00111002.jpg'],
    ]
    gr.Interface(
        get_text,
        inputs=['image'],
        outputs='text',
        title="imgocr: Image OCR",
        description="Input an image, and the machine will output the OCR result.",
        article="Link to <a href='https://github.com/shibing624/imgocr' style='color:blue;' target='_blank\'>Github REPO</a>",
        examples=examples
    ).launch()
