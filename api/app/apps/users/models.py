from tortoise import models, fields

class User(models.Model):
    id = fields.IntField(pk=True, description="用户ID")
    username = fields.CharField(max_length=255, unique=True, description="用户名")
    nickname = fields.CharField(max_length=255, index=True, description="昵称")
    password = fields.CharField(max_length=128, description="密码")
    openid = fields.CharField(max_length=255, unique=True, description="OpenID")
    mobile = fields.CharField(max_length=15,index=True, description="手机号")
    avatar = fields.CharField(max_length=255, null=True, description="头像")
    country = fields.CharField(max_length=255, null=True, description="国家")
    province = fields.CharField(max_length=255, null=True, description="省份")
    city = fields.CharField(max_length=255, null=True, description="城市")
    sex = fields.IntField(default=0, null=True, description="性别")
    creates_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")
    deleted_time = fields.DatetimeField(null=True, description="删除时间")
    # email = fields.CharField(max_length=100, unique=True)
    # is_active = fields.BooleanField(default=False)
    # is_superuser = fields.BooleanField(default=False)
    # created_at = fields.DatetimeField(auto_now_add=True)
    # updated_at = fields.DatetimeField(auto_now=True)

    # 元数据
    class Meta:
        table = "user_info"
        description = "用户信息"
        # ordering = ["-id"]
        # indexes = ["username", "nickname", "mobile"]

    def __repr__(self):
        return f"User (id={self.id}, username={self.username})"
    
    __str__ = __repr__