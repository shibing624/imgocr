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
[![python_version](https://img.shields.io/badge/Python-3.5%2B-green.svg)](requirements.txt)
[![GitHub issues](https://img.shields.io/github/issues/shibing624/imgocr.svg)](https://github.com/shibing624/imgocr/issues)
[![Wechat Group](https://img.shields.io/badge/wechat-group-green.svg?logo=wechat)](#Contact)


**imgocr**：Python3 package for Chinese/English OCR, with paddleocr-v4 onnx model(~14MB).

**imgocr**：基于PaddleOCR-v4-onnx模型（~14MB）推理，性能更高，可实现 CPU 上毫秒级的 OCR 精准预测，在通用场景上达到开源SOTA。


## Showcase


| 银行存根                                                                                                     | 表格                                                                                                        |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <img src="https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/00111002.jpg" width="400"> | <img src="https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/00015504.jpg" width="600">  |
| 火车票                                                                                                      | 英文论文                                                                                                      |
| <img src="https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/00056221.jpg" width="400"> | <img src="https://github.com/shibing624/imgocr/blob/main/examples/ocr_results/eng_paper.png" width="600"> |

## Benchmark

PP-OCRv4串联系统由文本检测模型和文本识别模型串联完成，首先输入预测图片，经过文本检测模型获取全部的检测框。根据检测框坐标在原图中抠出文本行，并进行矫正，最后将全部文本行送入文本识别模型，得到文本结果。

整个流程如下图所示：

<img src="https://github.com/shibing624/imgocr/blob/main/docs/ppocrv4_framework.png" width="800" alt="ppocr-v4">

OCR 检测/识别 benchmark：

| 模型               | 检测 mAP(%) | 识别 Acc(%) | GPU 推理耗时(ms) | CPU 推理耗时(ms) | 模型存储大小(M)  | 
|------------------|-----------|-----------|-----------------|------------------|------------|
| PP-OCRv4-mobile  | 77.79     | 78.20     | 2.719474        | 79.1097           | 14         | 


> GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32，CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为 8，精度类型为 FP32。

> OCR 评估集是 PaddleOCR 自建的中文数据集，覆盖街景、网图、文档、手写多个场景，其中文本识别包含1.1w张图片，检测包含500张图片。

## Demo

HuggingFace Demo: https://huggingface.co/spaces/shibing624/imgocr

![](https://github.com/shibing624/imgocr/blob/main/docs/hf.png)

run example: [examples/gradio_demo.py](https://github.com/shibing624/imgocr/blob/main/examples/gradio_demo.py) to see the demo:
```shell
python examples/gradio_demo.py
```

## Install
```shell
pip install -U imgocr
```

or

```shell
pip install -r requirements.txt
git clone https://github.com/shibing624/imgocr.git
cd imgocr
pip install --no-deps .
```

## Usage

### OCR识别

example: [examples/ocr_demo.py](https://github.com/shibing624/imgocr/blob/main/examples/ocr_demo.py)

```python
from imgocr import ImgOcr
m = ImgOcr()
result = m.ocr("data/11.jpg")
print("result:", result)
```

output:
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
