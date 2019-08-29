# steel-detect
数钢筋demo，IOU 0.7 下，AP 90.6。训练只要不到十分钟，可以非常愉快的玩耍
并且不需要任何预训练权重，完全从头训练。

文章链接：https://zhuanlan.zhihu.com/p/77034373

# 环境
1. 代码是在RFBNet官方代码基础上改的，非常推荐阅读和学习RFBNet的官方代码，非常简洁优雅易懂
按照RFB官方源码进行编译： https://github.com/ruinmessi/RFBNet

2. 将RFB编译好的utils里的文件夹build,nms替换数钢筋代码的utils/build,utils/nms即可

3. 修改data/config.py中的数据集路径`VOCroot = '/home/common/wangsong/SteelVOC'
` 改为自己数据集对应的路径

4. 运行train_RFB

# 训练好的网络权重
直接加群下载，欢迎加群交流，云深不知处-目标检测 763679865
