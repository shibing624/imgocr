# -*- coding: utf-8 -*-
import sys

from setuptools import setup, find_packages

# Avoids IDE errors, but actual version is read from version.py
__version__ = ""
exec(open('imgocr/version.py').read())

if sys.version_info < (3,):
    sys.exit('Sorry, Python3 is required.')

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

extras_require = {
    "onnxruntime": ["onnxruntime"],
    "onnxruntime-gpu": ["onnxruntime-gpu"],
    "serve": ["uvicorn[standard]", "fastapi", "python-multipart", "pydantic"],
    "dev": ["albumentations", "pip-tools", "pytest", "datasets[vision]"],
}

setup(
    name='imgocr',
    version=__version__,
    description='Image ocr tool, use ppocr onnx model.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='XuMing',
    author_email='xuming624@qq.com',
    url='https://github.com/shibing624/imgocr',
    license="Apache License 2.0",
    zip_safe=False,
    python_requires=">=3.6.0",
    entry_points={"console_scripts": ["imgocr = imgocr.cli:main"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords='ocr, image ocr, text recognition',
    install_requires=[
        "loguru",
        "tqdm",
        "shapely",
        "numpy",
        "pillow",
        "pyclipper",
        "requests",
        "opencv-python-headless",
    ],
    extras_require=extras_require,
    packages=find_packages(exclude=['tests']),
    package_dir={'imgocr': 'imgocr'},
    package_data={'imgocr': ['*.*', 'fonts/*.ttf', 'models/*.onnx', 'models/*.txt']},
)
