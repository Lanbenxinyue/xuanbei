import logging
from Common.dir_config import logs_dir


class LoggerHandler(logging.Logger):

    def __init__(self,name="Ui自动化日志",
                 level="DEBUG",
                 file=None,
                 format="%(name)s-%(asctime)s-%(levelname)s-%(lineno)d-%(message)s"):
        #logger = logging.getLogger(name)
        super().__init__(name)
        "设置级别"
        self.setLevel(level)

        fmt = logging.Formatter(format)

        "初始化处理器"
        if  file:
            file_handler = logging.FileHandler(file,encoding="utf-8")
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        Stream_handler = logging.StreamHandler()

        "设置处理器级别"
        Stream_handler.setLevel(level)
        Stream_handler.setFormatter(fmt)
        self.addHandler(Stream_handler)


logger = LoggerHandler("Ui自动化日志",file=logs_dir)
if __name__ == '__main__':
    log = LoggerHandler(file=logs_dir)
    log.debug("测试路径123")

