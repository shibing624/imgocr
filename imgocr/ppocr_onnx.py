# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: main module.
"""
from typing import Union, List
import argparse
from PIL import Image
import numpy as np
import cv2
import os

try:
    from cv2.typing import MatLike
except ImportError:
    from numpy import ndarray as MatLike
from .predict_system import TextSystem
from .utils import infer_args, draw_ocr, http_get

pwd_path = os.path.abspath(os.path.dirname(__file__))

__all__ = ['ImgOcr', 'draw_ocr_boxes', 'load_image']

MODEL_URLS = {
    "server": {
        "det": "https://modelscope.cn/models/lili666/imgocr/resolve/master/ch_PP-OCRv4_det_server_infer.onnx",
        "rec": "https://modelscope.cn/models/lili666/imgocr/resolve/master/ch_PP-OCRv4_rec_server_infer.onnx",
        "cls": "https://modelscope.cn/models/lili666/imgocr/resolve/master/ch_PP-OCRv4_cls_infer.onnx"
    },
    "mobile": {
        "det": "https://modelscope.cn/models/lili666/imgocr/resolve/master/ch_PP-OCRv4_det_mobile_infer.onnx",
        "rec": "https://modelscope.cn/models/lili666/imgocr/resolve/master/ch_PP-OCRv4_rec_mobile_infer.onnx",
        "cls": "https://modelscope.cn/models/lili666/imgocr/resolve/master/ch_PP-OCRv4_cls_infer.onnx"
    },
}


class ImgOcr(TextSystem):
    def __init__(self, **kwargs):
        parser = infer_args()
        inference_args_dict = {}
        for action in parser._actions:
            inference_args_dict[action.dest] = action.default
        params = argparse.Namespace(**inference_args_dict)
        # 根据传入的参数覆盖更新默认参数
        params.__dict__.update(**kwargs)

        # 选择模型，is_efficiency_mode=True 使用移动端模型，否则使用服务器端（大的）模型
        if not params.is_efficiency_mode:
            # 模型路径
            local_det_model_path = os.path.join(pwd_path, 'models/ch_PP-OCRv4_det_server_infer.onnx')
            if not os.path.exists(local_det_model_path):
                http_get(MODEL_URLS["server"]['det'], local_det_model_path)
            params.det_model_path = local_det_model_path
            local_rec_model_path = os.path.join(pwd_path, 'models/ch_PP-OCRv4_rec_server_infer.onnx')
            if not os.path.exists(local_rec_model_path):
                http_get(MODEL_URLS["server"]['rec'], local_rec_model_path)
            params.rec_model_path = local_rec_model_path

        # 初始化模型
        super().__init__(params)

    def ocr(self, img: Union[str, Image.Image, MatLike], det=True, rec=True, cls=True) -> List:
        """
        Perform OCR on the input image.

        Args:
            img: The input image in one of the following formats:
                - str: Path to the image file.
                - PIL.Image: A Python Imaging Library (PIL) image.
                - MatLike: A numpy array (as used by OpenCV).
            det: Whether to perform text detection.
            rec: Whether to perform text recognition.
            cls: Whether to perform text classification.

        Returns:
            The OCR result based on the detection, recognition, and classification.
        """
        img = load_image(img)

        if det and rec:
            dt_boxes, rec_res = self.__call__(img, cls)
            ocr_res = [{'box': box.tolist(), 'text': res[0], 'score': res[1]} for box, res in zip(dt_boxes, rec_res)]
            return ocr_res
        elif det and not rec:
            dt_boxes = self.text_detector(img)
            ocr_res = [{'box': box.tolist()} for box in dt_boxes]
            return ocr_res
        else:
            if not isinstance(img, list):
                img = [img]
            if self.use_angle_cls and cls:
                img, cls_res_tmp = self.text_classifier(img)
            rec_res = self.text_recognizer(img)
            ocr_res = [{'text': res[0], 'score': res[1]} for res in rec_res]
            return ocr_res


def load_image(img: Union[str, Image.Image, MatLike]) -> np.ndarray:
    """
    Load an image from a file path, PIL image, or numpy array.

    Args:
        img: The input image in one of the following formats:
            - str: Path to the image file.
            - PIL.Image: A Python Imaging Library (PIL) image.
            - MatLike: A numpy array (as used by OpenCV).

    Returns:
        The loaded image as a numpy array.
    """
    if isinstance(img, str):
        img_path = img
        img = cv2.imread(img_path)
        if img is None:
            raise FileNotFoundError(f"The image file is not found: {img_path}")
    elif isinstance(img, Image.Image):
        img = np.array(img)
        img = img[:, :, ::-1]  # Convert RGB to BGR
    elif isinstance(img, MatLike):
        if img.size == 0:
            raise ValueError("The input image is empty")
    else:
        raise TypeError(f"Unsupported input type: {type(img)}. "
                        f"Supported types are str, PIL.Image, and numpy.ndarray.")
    return img


def draw_ocr_boxes(origin_img: Union[str, Image.Image, MatLike], ocr_result: List[dict], saved_img_path="draw_ocr.jpg"):
    """
    Draw the OCR results on the input image and save the result.

    Args:
        origin_img: The input image in one of the following formats:
            - str: Path to the image file.
            - PIL.Image: A Python Imaging Library (PIL) image.
            - MatLike: A numpy array (as used by OpenCV).
        ocr_result: The OCR result as a list of dictionaries with keys 'box', 'text', and 'score'.
        saved_img_path: The path to save the image with drawn OCR results.

    Returns:
        The image with drawn OCR results as a numpy array.
    """
    origin_img = load_image(origin_img)
    # Convert BGR to RGB for drawing
    img = origin_img[:, :, ::-1]
    boxes = [res['box'] for res in ocr_result]
    txts = [res['text'] for res in ocr_result]
    scores = [res['score'] for res in ocr_result]
    im_show = draw_ocr(img, boxes, txts, scores)
    # Convert back from RGB to BGR for displaying and saving with cv2
    im_show = im_show[:, :, ::-1]
    cv2.imwrite(saved_img_path, im_show)
    return im_show
