import os, time
from .logs import get_logger


logger = get_logger(os.environ.get("APP_NAME", "ai_wechat"))


async def log_requests(request, call_next):
    start_time = time.time()
    logger.info(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} {request.method} {request.url.path}")
    response = await call_next(request)
    process_time = time.time() - start_time
    formatted_process_time = "{0:.2f}".format(process_time*1000)
    logger.info(f"path={request.url.path} method={request.method} status_code={response.status_code} process_time={formatted_process_time}ms")
    return response