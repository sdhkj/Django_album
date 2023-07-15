from django.db import models

# Create your models here.
# /photo/models.py

from django.db import models
from django.utils.timezone import now

class Photo(models.Model):

    # ImageField 字段用于存储图片信息 ImageField
    # 实际上只在数据库中保存了图片的名称、存储路径、索引等元数据，真正的图片文件被保存在 upload_to 参数所指定的路径中。
    image   = models.ImageField(upload_to='photo/%Y%m%d/')
    # DateTimeField
    # 用于记录图片创建的时间，默认值为当前时间
    created = models.DateTimeField(default=now)

    # __str__方法
    # 用于美化模型在后台、命令行中的输出信息
    def __str__(self):
        return self.image.name

    #Photo 模型增加一个 Meta 内部类
    #ordering 属性定义了图片数据的排序，比如这里是按创建时间倒序排列
    class Meta:
        ordering = ('-created',)

