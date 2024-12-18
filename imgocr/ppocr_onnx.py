# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: main module.
"""
from typing import Union, List
import argparse
import PIL
from PIL import Image
import numpy as np
import cv2
from cv2.typing import MatLike
from loguru import logger
from .predict_system import TextSystem
from .utils import infer_args
from .utils import draw_ocr


class ImgOcr(TextSystem):
    def __init__(self, **kwargs):
        parser = infer_args()
        inference_args_dict = {}
        for action in parser._actions:
            inference_args_dict[action.dest] = action.default
        params = argparse.Namespace(**inference_args_dict)
        # 根据传入的参数覆盖更新默认参数
        params.__dict__.update(**kwargs)
        # 初始化模型
        super().__init__(params)

    def ocr(self, img: Union[str, PIL.Image.Image, MatLike], det=True, rec=True, cls=True):
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

        if cls and not self.use_angle_cls:
            logger.debug("Since the angle classifier is not initialized, "
                         "the angle classifier will not be uesd during the forward process")
        if det and rec:
            ocr_res = []
            dt_boxes, rec_res = self.__call__(img, cls)
            tmp_res = [[box.tolist(), res] for box, res in zip(dt_boxes, rec_res)]
            ocr_res.append(tmp_res)
            return ocr_res
        elif det and not rec:
            ocr_res = []
            dt_boxes = self.text_detector(img)
            tmp_res = [box.tolist() for box in dt_boxes]
            ocr_res.append(tmp_res)
            return ocr_res
        else:
            ocr_res = []
            cls_res = []

            if not isinstance(img, list):
                img = [img]
            if self.use_angle_cls and cls:
                img, cls_res_tmp = self.text_classifier(img)
                if not rec:
                    cls_res.append(cls_res_tmp)
            rec_res = self.text_recognizer(img)
            ocr_res.append(rec_res)

            if not rec:
                return cls_res
            return ocr_res


def load_image(img: Union[str, PIL.Image.Image, MatLike]) -> np.ndarray:
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
    elif isinstance(img, PIL.Image.Image):
        img = np.array(img)
        img = img[:, :, ::-1]  # Convert RGB to BGR
    elif isinstance(img, MatLike):
        if img.size == 0:
            raise ValueError("The input image is empty")
    else:
        raise TypeError(f"Unsupported input type: {type(img)}. "
                        f"Supported types are str, PIL.Image, and numpy.ndarray.")
    return img


def drwa_ocr_boxes(origin_img, ocr_result, saved_img_path="draw_ocr.jpg"):
    """
    Draw the OCR results on the input image and save the result.
    :param origin_img:
    :param ocr_result:
    :param saved_img_path:
    :return:
    """
    origin_img = load_image(origin_img)
    ocr_result = ocr_result[0]
    # Convert BGR to RGB for drawing
    img = origin_img[:, :, ::-1]
    boxes = [line[0] for line in ocr_result]
    txts = [line[1][0] for line in ocr_result]
    scores = [line[1][1] for line in ocr_result]
    im_show = draw_ocr(img, boxes, txts, scores)
    # Convert back from RGB to BGR for displaying and saving with cv2
    im_show = im_show[:, :, ::-1]
    cv2.imwrite(saved_img_path, im_show)
    return im_show
