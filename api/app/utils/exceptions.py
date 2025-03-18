from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import status

def global_http_exception_handler(request, exc):
    '''
    全局异常处理

    '''
    # print(f"发生异常： {exc}")
    return JSONResponse({
        "code": exc.status_code,
        "message": exc.detail,
        "status":"Failed"
    })

def global_request_exception_handler(request, exc):
    '''
    全局异常处理

    '''
    
    return JSONResponse({
        "code": status.HTTP_400_BAD_REQUEST,
        "message": exc.errors()[0],
        "status":"Failed"
    })