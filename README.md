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


**imgocr**：Python3 package for Chinese/English OCR, with paddleocr-v4/paddleocr-v5 onnx model(~16MB).

**imgocr**：基于PaddleOCR-v5-onnx模型（~16MB）推理，性能更高，可实现 CPU 上毫秒级的 OCR 精准预测，在通用场景上达到开源SOTA。


## Showcase


| 银行存根 | ![银行存根](https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/00111002.jpg) |
|----------|----------------------------------------------------------------------------------------------|
| 表格     | ![表格](https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/00015504.jpg)     |
| 火车票   | ![火车票](https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/00056221.jpg)   |
| 英文论文 | ![英文论文](https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/eng_paper.png) |

## Benchmark

PP-OCRv4串联系统由文本检测模型和文本识别模型串联完成，首先输入预测图片，经过文本检测模型获取全部的检测框。根据检测框坐标在原图中抠出文本行，并进行矫正，最后将全部文本行送入文本识别模型，得到文本结果。

整个流程如下图所示：

<img src="https://github.com/shibing624/imgocr/blob/main/docs/ppocrv4_framework.png" width="800" alt="ppocr-v4">

OCR 检测/识别 benchmark：

| 模型                     | 检测 mAP(%) | 识别 Acc(%) | GPU 推理耗时(ms) | CPU 推理耗时(ms) | 模型存储大小(MB) | 下载地址 |
|------------------------|-----------|-----------|--------------|--------------|------------|--------|
| PP-OCRv4-mobile(高效率)   | 63.8      | 78.74     | 2.71         | 79.11        | 14         | [mobile-model](https://modelscope.cn/models/lili666/imgocr/summary) |
| PP-OCRv4-server(高精度)	  | 69.2	     | 85.19	    | 24.92	       | 2742.31	     | 207        | [server-model](https://modelscope.cn/models/lili666/imgocr/summary) |
| PP-OCRv5-mobile(高效率，默认)	 | 79.0	     | 81.29	    | 6.36	        | 82.11	       | 20         | [server-model](https://modelscope.cn/models/lili666/imgocr/summary) |
| PP-OCRv5-server(高精度)	  | 83.8	     | 86.38	    | 28.15	       | 2900.12	     | 160        | [server-model](https://modelscope.cn/models/lili666/imgocr/summary) |


> GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32，CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，精度类型为 FP32。

> OCR 评估集是 PaddleOCR 自建的中文数据集，覆盖街景、网图、文档、手写多个场景，其中文本识别包含1.1w张图片，检测包含500张图片。



## Demo

HuggingFace Demo: https://huggingface.co/spaces/shibing624/imgocr

![](https://github.com/shibing624/imgocr/blob/main/docs/imgocr_hf.png)

run example: [examples/gradio_demo.py](https://github.com/shibing624/imgocr/blob/main/examples/gradio_demo.py) to see the demo:
```shell
python examples/gradio_demo.py
```

## Install

无需安装paddlepaddle、paddleocr等深度学习库，仅需安装onnxruntime，即可用imgocr调用。

```shell
pip install onnxruntime # pip install onnxruntime-gpu for gpu
pip install imgocr
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

> `is_efficiency_mode`: 是否使用高效率模型，默认`True`，使用高效率模型(mobile，16MB)，速度更快，精度稍低，该模型已经内置集成在`imgocr/models`文件夹下。如果需要更高精度，设置为False，使用高精度模型(server，160MB)，代码会自动下载到`imgocr/models`文件夹。

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

### 命令行模式（CLI）

支持批量做OCR识别

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
