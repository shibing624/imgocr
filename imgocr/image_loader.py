# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
from typing import Union
from pathlib import Path
from io import BytesIO
import numpy as np
import cv2
from PIL import Image, UnidentifiedImageError

MatLike = np.ndarray


def load_image(img: Union[str, Image.Image, MatLike, Path, bytes]) -> np.ndarray:
    """
    Load an image from a file path, PIL image, numpy array, Path object, or bytes.

    Args:
        img: The input image in one of the following formats:
            - str: Path to the image file.
            - PIL.Image: A Python Imaging Library (PIL) image.
            - MatLike: A numpy array (as used by OpenCV).
            - Path: A pathlib.Path object pointing to the image file.
            - bytes: Image data in bytes.

    Returns:
        The loaded image as a numpy array.
    """
    if isinstance(img, (str, Path)):
        img_path = str(img)
        if not Path(img_path).exists():
            raise Exception(f"The image file is not found: {img_path}")
        try:
            img = Image.open(img_path)
        except UnidentifiedImageError as e:
            raise Exception(f"Cannot identify image file {img_path}") from e
        img = img_to_ndarray(img)
    elif isinstance(img, bytes):
        try:
            img = Image.open(BytesIO(img))
        except UnidentifiedImageError as e:
            raise Exception("Cannot identify image from bytes") from e
        img = img_to_ndarray(img)
    elif isinstance(img, Image.Image):
        img = img_to_ndarray(img)
    elif isinstance(img, MatLike):
        if img.size == 0:
            raise ValueError("The input image is empty")
    else:
        raise TypeError(
            f"Unsupported input type: {type(img)}. Supported types are str, PIL.Image, numpy.ndarray, Path, and bytes.")

    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    elif img.ndim == 3:
        if img.shape[2] == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        elif img.shape[2] == 4:
            img = cvt_four_to_three(img)
        elif img.shape[2] == 2:
            img = cvt_two_to_three(img)
        elif img.shape[2] != 3:
            raise Exception(f"The channel({img.shape[2]}) of the img is not in [1, 2, 3, 4]")
    else:
        raise Exception(f"The ndim({img.ndim}) of the img is not in [2, 3]")

    return img


def img_to_ndarray(img: Image.Image) -> np.ndarray:
    # Convert the image to grayscale if it is in binary mode
    if img.mode == "1":
        img = img.convert("L")
    return np.array(img)


def cvt_two_to_three(img: np.ndarray) -> np.ndarray:
    """gray + alpha → BGR"""
    img_gray = img[..., 0]
    img_bgr = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

    img_alpha = img[..., 1]
    not_a = cv2.bitwise_not(img_alpha)
    not_a = cv2.cvtColor(not_a, cv2.COLOR_GRAY2BGR)

    new_img = cv2.bitwise_and(img_bgr, img_bgr, mask=img_alpha)
    new_img = cv2.add(new_img, not_a)
    return new_img


def cvt_four_to_three(img: np.ndarray) -> np.ndarray:
    """RGBA → BGR"""
    r, g, b, a = cv2.split(img)
    new_img = cv2.merge((b, g, r))

    not_a = cv2.bitwise_not(a)
    not_a = cv2.cvtColor(not_a, cv2.COLOR_GRAY2BGR)

    new_img = cv2.bitwise_and(new_img, new_img, mask=a)

    mean_color = np.mean(new_img)
    if mean_color <= 0.0:
        new_img = cv2.add(new_img, not_a)
    else:
        new_img = cv2.bitwise_not(new_img)
    return new_img