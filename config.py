import os

from qfluentwidgets import QConfig

import log

__version__ = "0.1.0"
__url__ = "https://github.com/JunNanLYS/Apex_Assistant"
abspath = os.path.dirname(os.path.abspath(__file__))  # project root path


class Config(QConfig):
    pass


cfg = Config()

log.info(f"版本号{__version__}")
log.info(f"该项目为公益免费开源项目，若从github外使用金钱购买请立即差评并举报商家，github地址为{__url__}")
