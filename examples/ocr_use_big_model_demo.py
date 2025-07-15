# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: Image ocr demo.
"""
import time
import sys

sys.path.append('..')
from imgocr import ImgOcr

if __name__ == "__main__":
    m = ImgOcr(use_gpu=False, model_version='v5', is_efficiency_mode=True)
    img_path = "data/hard1.jpg"
    s = time.time()
    result = m.ocr(img_path)
    e = time.time()
    print("total time: {:.4f} s".format(e - s))
    print("result:", result)
    for line in result:
        print(line['text'])

    print('-------------------\n')

    m = ImgOcr(use_gpu=False, is_efficiency_mode=False, model_version='v5')
    s = time.time()
    result = m.ocr(img_path)
    e = time.time()
    print("total time: {:.4f} s".format(e - s))
    print("result:", result)
    for line in result:
        print(line['text'])

"""
# v4-mobile
正品促销
大桶装更划算
强力去污符合国标
-40℃深度防冻不结冰
10.0起
10.0起
5.8起
券后价?
惊喜福利不容错过
极速发货
冰点标准
破损就赔
假一赔十

# v4-server
正品促销
大桶装更划算
强力去污符合国标
-40°C深度防冻不结冰
10.0起
日常价￥
直击
10.0起
底价
5.8
券后价￥
起
惊喜福利不容错过
极速发货
冰点标准
破损就赔
假一赔十

# v5-mobile
正品促销
大桶装 更划算
强力去污符合国标
-40°℃深度防冻不结冰
10.0起
日常
真击
底价
10.0起
5.8
券后价￥
起
惊喜福利不容错过
极速发货
冰点标准
破损就赔
假一赔十

# v5-server
正品促销
大桶装更划算
强力去污符合国标
-40℃深度防冻不结冰
日常价
直击
10.0起
10.0起
日常价￥
底价
5.8
券后价￥
起
惊喜福利不容错过
极速发货
冰点标准
破损就赔
假一赔十
"""
