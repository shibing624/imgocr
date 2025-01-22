[**🇨🇳中文**](https://github.com/shibing624/imgocr/blob/main/README.md) | [**🌐English**](https://github.com/shibing624/imgocr/blob/main/README_EN.md) | [**📖文档/Docs**](https://github.com/shibing624/imgocr/wiki) 

<div align="center">
  <a href="https://github.com/shibing624/imgocr">
    <img src="https://github.com/shibing624/imgocr/blob/main/docs/imgocr-logo.png" height="150" alt="Logo">
  </a>
</div>

-----------------

# imgocr: Image OCR toolkit
[![PyPI version](https://badge.fury.io/py/imgocr.svg)](https://badge.fury.io/py/imgocr)
[![Downloads](https://static.pepy.tech/badge/imgocr)](https://pepy.tech/project/imgocr)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![python_version](https://img.shields.io/badge/Python-3.6%2B-green.svg)](requirements.txt)
[![GitHub issues](https://img.shields.io/github/issues/shibing624/imgocr.svg)](https://github.com/shibing624/imgocr/issues)
[![Wechat Group](https://img.shields.io/badge/wechat-group-green.svg?logo=wechat)](#Contact)

**imgocr**: Python3 package for Chinese/English OCR, with paddleocr-v4 onnx model(~14MB).

**imgocr**: Based on the PaddleOCR-v4-onnx model (~14MB) reasoning, it has higher performance and can achieve millisecond-level OCR accurate prediction on CPU, reaching open source SOTA in general scenarios.

## Showcase


| 银行存根 | ![银行存根](https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/00111002.jpg) |
|----------|----------------------------------------------------------------------------------------------|
| 表格     | ![表格](https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/00015504.jpg)     |
| 火车票   | ![火车票](https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/00056221.jpg)   |
| 英文论文 | ![英文论文](https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/eng_paper.png) |

## Benchmark

The PP-OCRv4 tandem system is completed by the tandem of the text detection model and the text recognition model. First, the predicted image is input, and all the detection frames are obtained through the text detection model. According to the coordinates of the detection frame, the text lines are cut out from the original image and corrected. Finally, all the text lines are sent to the text recognition model to obtain the text results.

The whole process is shown in the figure below:

<img src="https://github.com/shibing624/imgocr/blob/main/docs/ppocrv4_framework.png" width="800" alt="ppocr-v4">

OCR detection/recognition benchmark:

| Model | Detection mAP(%) | Recognition Acc(%) | GPU inference time(ms) | CPU inference time(ms) | Model storage size(M) | Download |
|------------------|-----------|-----------|----------------|------------------|------------|---------|
| PP-OCRv4-mobile(高效率，默认) | 77.79     | 78.20     | 2.71         | 79.11        | 14        | [mobile-model](https://modelscope.cn/models/lili666/imgocr/summary) |
| PP-OCRv4-server(高精度)	   | 82.69	    | 84.04	    | 24.92	       | 2742.31	     | 207       | [server-model](https://modelscope.cn/models/lili666/imgocr/summary) |

> GPU inference time is based on NVIDIA Tesla T4 machine, precision type is FP32, CPU inference speed is based on Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz, precision type is FP32.

> The OCR evaluation set is a Chinese dataset built by PaddleOCR, covering multiple scenes such as street scenes, web images, documents, and handwriting. The text recognition contains 11,000 pictures and the detection contains 500 pictures.

## Demo

HuggingFace Demo: https://huggingface.co/spaces/shibing624/imgocr

![](https://github.com/shibing624/imgocr/blob/main/docs/imgocr_hf.png)

run example: [examples/gradio_demo.py](https://github.com/shibing624/imgocr/blob/main/examples/gradio_demo.py) to see the demo:
```shell
python examples/gradio_demo.py
```

## Install
No need to install deep learning libraries such as paddlepaddle and paddleocr, just install onnxruntime and you can use imgocr to call it.

```shell
pip install onnxruntime # pip install onnxruntime-gpu for gpu
pip install -U imgocr
```

or

```shell
git clone https://github.com/shibing624/imgocr.git
cd imgocr
pip install onnxruntime # pip install onnxruntime-gpu for gpu
pip install -r requirements.txt
pip install .
```

## Usage

### OCR识别

example: [examples/ocr_demo.py](https://github.com/shibing624/imgocr/blob/main/examples/ocr_demo.py)

```python
from imgocr import ImgOcr
m = ImgOcr(use_gpu=False, is_efficiency_mode=True)
result = m.ocr("data/11.jpg")
print("result:", result)
for i in result:
    print(i['text'])
```

> `is_efficiency_mode`: Whether to use the high-efficiency model, the default is `True`, using the high-efficiency model (mobile, 14MB), which is faster and slightly less accurate. This model has been built-in and integrated in the `imgocr/models` folder. If higher accuracy is required, set it to False, use the high-precision model (server, 207MB), and the code will be automatically downloaded to the `imgocr/models` folder.

output:
```shell
result: [{'box': [[28.0, 37.0], [302.0, 39.0], [302.0, 72.0], [27.0, 70.0]], 'text': '纯臻营养护发素', 'score': 0.9978395700454712}, {'box': [[26.0, 83.0], [173.0, 83.0], [173.0, 104.0], [26.0, 104.0]], 'text': '产品信息/参数', 'score': 0.9898329377174377}, {'box': [[27.0, 112.0], [331.0, 112.0], [331.0, 135.0], [27.0, 135.0]], 'text': '（45元/每公斤，100公斤起订）', 'score': 0.9659210443496704}, {'box': [[25.0, 143.0], [281.0, 143.0], [281.0, 165.0], [25.0, 165.0]], 'text': '每瓶22元，1000瓶起订）', 'score': 0.9928666353225708}, {'box': [[26.0, 179.0], [300.0, 179.0], [300.0, 195.0], [26.0, 195.0]], 'text': '【品牌】：代加工方式/OEMODM', 'score': 0.9843945503234863}, {'box': [[26.0, 210.0], [234.0, 210.0], [234.0, 227.0], [26.0, 227.0]], 'text': '【品名】：纯臻营养护发素', 'score': 0.9963161945343018}, {'box': [[25.0, 239.0], [241.0, 239.0], [241.0, 259.0], [25.0, 259.0]], 'text': '【产品编号】：YM-X-3011', 'score': 0.9848018884658813}, {'box': [[413.0, 232.0], [430.0, 232.0], [430.0, 306.0], [413.0, 306.0]], 'text': 'ODMOEM', 'score': 0.9908049702644348}, {'box': [[24.0, 271.0], [180.0, 271.0], [180.0, 290.0], [24.0, 290.0]], 'text': '【净含量】：220ml', 'score': 0.9892324209213257}, {'box': [[26.0, 303.0], [251.0, 303.0], [251.0, 319.0], [26.0, 319.0]], 'text': '【适用人群】：适合所有肤质', 'score': 0.9909228682518005}, {'box': [[26.0, 335.0], [344.0, 335.0], [344.0, 352.0], [26.0, 352.0]], 'text': '【主要成分】：鲸蜡硬脂醇、燕麦β-葡聚', 'score': 0.9828647971153259}, {'box': [[26.0, 364.0], [281.0, 364.0], [281.0, 384.0], [26.0, 384.0]], 'text': '糖、椰油酰胺丙基甜菜碱、泛醌', 'score': 0.9505177140235901}, {'box': [[368.0, 368.0], [477.0, 368.0], [477.0, 389.0], [368.0, 389.0]], 'text': '（成品包材）', 'score': 0.992072343826294}, {'box': [[26.0, 397.0], [360.0, 397.0], [360.0, 414.0], [26.0, 414.0]], 'text': '【主要功能】：可紧致头发磷层，从而达到', 'score': 0.9904329180717468}, {'box': [[28.0, 429.0], [370.0, 429.0], [370.0, 445.0], [28.0, 445.0]], 'text': '即时持久改善头发光泽的效果，给干燥的头', 'score': 0.9874186515808105}, {'box': [[27.0, 458.0], [137.0, 458.0], [137.0, 479.0], [27.0, 479.0]], 'text': '发足够的滋养', 'score': 0.9987384676933289}]
纯臻营养护发素
产品信息/参数
（45元/每公斤，100公斤起订）
每瓶22元，1000瓶起订）
【品牌】：代加工方式/OEMODM
【品名】：纯臻营养护发素
【产品编号】：YM-X-3011
ODMOEM
【净含量】：220ml
【适用人群】：适合所有肤质
【主要成分】：鲸蜡硬脂醇、燕麦β-葡聚
糖、椰油酰胺丙基甜菜碱、泛醌
（成品包材）
【主要功能】：可紧致头发磷层，从而达到
即时持久改善头发光泽的效果，给干燥的头
发足够的滋养
```
![](https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/11.jpg)

### Command Line Interface(CLI)

Supports batch OCR recognition

code: [cli.py](https://github.com/shibing624/imgocr/blob/main/imgocr/cli.py)

```
> imgocr -h                                    
usage: cli.py [-h] --image_dir IMAGE_DIR [--output_dir OUTPUT_DIR]
              [--chunk_size CHUNK_SIZE] [--use_gpu USE_GPU]

imgocr cli

options:
  -h, --help            show this help message and exit
  --image_dir IMAGE_DIR
                        input image dir path, required
  --output_dir OUTPUT_DIR
                        output ocr result dir path, default outputs
  --chunk_size CHUNK_SIZE
                        chunk size, default 10
  --use_gpu USE_GPU     use gpu, default False
```

run：

```shell
pip install imgocr -U
imgocr --image_dir data
```

> 输入图片目录（--image_dir， required）

## Contact

- Issue(建议)：[![GitHub issues](https://img.shields.io/github/issues/shibing624/imgocr.svg)](https://github.com/shibing624/imgocr/issues)
- 邮件我：xuming: xuming624@qq.com
- 微信我：加我*微信号：xuming624, 备注：姓名-公司-NLP* 进NLP交流群。

<img src="https://github.com/shibing624/imgocr/blob/main/docs/wechat.jpeg" width="200" />


## Citation

如果你在研究中使用了imgocr，请按如下格式引用：

APA:
```latex
Xu, M. imgocr: Image OCR toolkit (Version 0.0.1) [Computer software]. https://github.com/shibing624/imgocr
```

BibTeX:
```latex
@misc{imgocr,
  author = {Ming Xu},
  title = {imgocr: Image OCR toolkit},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/shibing624/imgocr}},
}
```

## License


授权协议为 [The Apache License 2.0](LICENSE)，可免费用做商业用途。请在产品说明中附加imgocr的链接和授权协议。


## Contribute
项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：

 - 在`tests`添加相应的单元测试
 - 使用`python -m pytest -v`来运行所有单元测试，确保所有单测都是通过的

之后即可提交PR。

## References
- [RapidOCR](https://github.com/RapidAI/RapidOCR)  
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)  
- [Paddle2ONNX](https://github.com/PaddlePaddle/Paddle2ONNX)
- [ppocr-onnx](https://github.com/triwinds/ppocr-onnx)
