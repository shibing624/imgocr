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

| Model | Detection mAP(%) | Recognition Acc(%) | GPU inference time(ms) | CPU inference time(ms) | Model storage size(M) |
|------------------|-----------|-----------|----------------|------------------|------------|
| PP-OCRv4-mobile | 77.79 | 78.20 | 2.719474 | 79.1097 | 14 |
| PP-OCRv4-server	   | 82.69	    | 84.04	    | 24.92	       | 2742.31	     | 207       | 

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
pip install onnxruntime # pip install onnxruntime-gpu for gpu
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
m = ImgOcr(use_gpu=False)
result = m.ocr("data/11.jpg")
print("result:", result)
```

output:
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
