# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: pip install paddlepaddle paddleocr -U

"""
from paddleocr import PaddleOCR

# 通过 text_detection_model_dir 指定本地模型路径
pipeline = PaddleOCR(
    use_doc_orientation_classify=False, # 通过 use_doc_orientation_classify 参数指定不使用文档方向分类模型
    use_doc_unwarping=False, # 通过 use_doc_unwarping 参数指定不使用文本图像矫正模型
    use_textline_orientation=False, # 通过 use_textline_orientation 参数指定不使用文本行方向分类模型
)

# 默认使用 PP-OCRv5_server_det 模型作为默认文本检测模型，如果微调的不是该模型，通过 text_detection_model_name 修改模型名称
# pipeline = PaddleOCR(text_detection_model_name="PP-OCRv5_mobile_det", text_detection_model_dir="./your_v5_mobile_det_model_path")

result = pipeline.predict("data/11.jpg")
# print(result)
for res in result:
    # res.print()
    r = res.get('rec_texts')
    print(r)
    # res.save_to_img("output")
    # res.save_to_json("output")

# ocr = PaddleOCR(
#     use_doc_orientation_classify=False, # 通过 use_doc_orientation_classify 参数指定不使用文档方向分类模型
#     use_doc_unwarping=False, # 通过 use_doc_unwarping 参数指定不使用文本图像矫正模型
#     use_textline_orientation=False, # 通过 use_textline_orientation 参数指定不使用文本行方向分类模型
# )
# # ocr = PaddleOCR(lang="en") # 通过 lang 参数来使用英文模型
# # ocr = PaddleOCR(ocr_version="PP-OCRv4") # 通过 ocr_version 参数来使用 PP-OCR 其他版本
# # ocr = PaddleOCR(device="gpu") # 通过 device 参数使得在模型推理时使用 GPU
# # ocr = PaddleOCR(
# #     text_detection_model_name="PP-OCRv5_server_det",
# #     text_recognition_model_name="PP-OCRv5_server_rec",
# #     use_doc_orientation_classify=False,
# #     use_doc_unwarping=False,
# #     use_textline_orientation=False,
# # ) # 更换 PP-OCRv5_server 模型
# result = ocr.predict("./general_ocr_002.png")
# for res in result:
#     res.print()
#     res.save_to_img("output")
#     res.save_to_json("output")