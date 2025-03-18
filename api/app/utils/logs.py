import logging , os
from logging import handlers, Logger

def get_logger(name: str="root") -> Logger:
    logger: Logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # 写入日志到终端
        th: logging.StreamHandler = logging.StreamHandler()
        try:
            os.mkdir("logs")
        except:
            pass
        # 写入日志到文件
        rf: handlers.RotatingFileHandler = handlers.RotatingFileHandler(
            filename=f"logs/{name}.log",
            mode="a",
            maxBytes=1024*1024*300,
            backupCount=10,
            encoding="utf-8"
        )
        # 设置日志级别
        th.setLevel(logging.DEBUG)
        rf.setLevel(logging.INFO)
        # 日志格式
        simple_formatter:logging.Formatter = logging.Formatter(
            fmt="{levelname} {asctime} {pathname}:{lineno} {message}",
            style="{",
        )
        verbose_formatter:logging.Formatter = logging.Formatter(
            fmt="【{name}】{levelname} {asctime} {pathname}:{lineno} {message}",
            datefmt="%Y-%m-%d %H:%M:%S",
            style="{",
        )
        # 添加日志格式
        th.setFormatter(simple_formatter)
        rf.setFormatter(verbose_formatter)
        # 添加handler
        logger.addHandler(th)
        logger.addHandler(rf)

    #     handler = logging.StreamHandler()
    #     handler.setLevel(logging.DEBUG)
    #     handler.setFormatter(formatter)
    #     logger.addHandler(handler)

    # formatter = logging.Formatter(
    #     '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    # )
    # handler = handlers.TimedRotatingFileHandler(
    #     filename=f'logs/{name}.log',
    #     when='midnight',
    #     interval=1,
    #     backupCount=7
    # )
    # handler.setLevel(logging.DEBUG)
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)
    return logger


if __name__ == "__main__":
    logger = get_logger("ai_wechat")
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

    # 单例模式
    logger1 = get_logger("ai_wechat")
    logger1.debug("debug")
    print(logger == logger1)