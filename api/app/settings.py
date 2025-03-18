import os

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",  # 修正引擎名称（原图片中Lysql应为mysql）
            "credentials": {
                "host": os.environ.get("DB_HOST", "127.0.0.1"),  # 数据库IP/域名地址
                "port": int(os.environ.get("DB_PORT", 3306)),  # 端口
                "user": os.environ.get("DB_USERNAME", "ai_wechat"),  # 连接账户
                "password": os.environ.get("DB_PASSWORD", "ai_wechat"),  # 连接密码
                "database": os.environ.get("DB_DATABASE", "ai_wechat"),  # 数据库名
                "charset": os.environ.get("DB_CHARSET", "utf8mb4"),  # 编码
                "minsize": int(os.environ.get("DB_POOL_MINSIZE", 10)),  # 连接池最小连接数
                "maxsize": int(os.environ.get("DB_POOL_MAXSIZE", 30)),  # 连接池最大连接数
                "echo": bool(os.environ.get("DEBUG", True))  # 是否打印SQL语句
            }
        }
    },
    "apps": {
        "models": {  # 应用配置（可自定义应用名，此处以"models"为例）
            "models": ["app.apps.users.models", "aerich.models"],  # 模型所在模块路径，需根据项目实际结构调整
            "default_connection": "default"  # 关联默认数据库连接
        }
    },
    "use_tz": False,  # 是否使用时区
    "timezone": os.environ.get("APP_TIMEZONE", "Asia/Shanghai")  # 时区设置
}