# config.py
import os.path


VOCroot = '/home/common/wangsong/SteelVOC'

# 90.57
#RFB CONFIGS
VOC_Config = {
    'feature_maps' : [52, 26, 13],

    'min_dim' : 416,

    'steps' : [8, 16, 32],

    'min_sizes' : [20, 40, 60],

    'aspect_ratios' : [[0.9],
                       [0.9],
                       [0.8]],

    'variance' : [0.1, 0.2],

    'clip' : True,
}


