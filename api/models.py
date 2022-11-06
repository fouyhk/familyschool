from django.db import models


class FUSER(models.Model):

    # 由雪花算法生成
    uid = models.BigIntegerField(name='u_id', verbose_name='用户id', primary_key=False, null=False)
    # 用户openid最长为30,大于官网所公布的28位
    openid = models.CharField(max_length=30, name='open_id', verbose_name='用户openid', null=False)
    # 用户昵称最长为10位
    usernc = models.CharField(max_length=10, name='u_nc', verbose_name='用户昵称', null=False)
    # 头像路径为绝对路径 "https://thirdwx.qlogo.cn/mmopen/vi_32
    # /POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132"
    touxiang = models.CharField(max_length=200, name='t_x', verbose_name='用户头像', null=False)
    # 注册时间格式为 YYYY/MM/DD HH/MM/SS
    createtime = models.DateTimeField(name='c_t', verbose_name='用户注册时间', null=False)
    # 从schooladdress中取出我们所需学校
    schoolid = models.IntegerField(name='s_id', verbose_name='学校id', null=False)
    # 用户协议 0->同意,1->不同意
    agreement = models.IntegerField(name='a_g', verbose_name='用户协议同意情况', null=False)
    # 用户签到积分,默认为0,与用户等级挂钩
    ustar = models.IntegerField(name='u_st', verbose_name='用户签到积分', null=False, default=0)
    # 用户状态 0->正常 1->封禁
    ustatus = models.IntegerField(name='u_sta', verbose_name='用户账号状态', null=False, default=0)
    # 用户用来绑定微信的手机号
    userPhone = models.BigIntegerField(name='u_p', verbose_name='用户手机', null=False)
    # 用户地址在库中的标识
    addreesid = models.IntegerField(name='a_id', verbose_name='用户收货地址id', null=True)
    # 主要用来帮助我们约束用户修改信息的最大次数
    updateTime = models.DateTimeField(name='u_t', verbose_name='用户信息更新时间', null=True)
    # 主要用来帮助我们对用户封禁之后的解封事宜
    lastTime = models.DateTimeField(name='l_t', verbose_name='用户最后一次登录时间', null=True)
    # 0 -> 男 1-> 女 2-> 未知
    userSex = models.IntegerField(name='u_s', verbose_name='用户性别', null=False, default=0)
    # 用户等级,默认为0级
    userRank = models.IntegerField(name='u_r', verbose_name='用户等级', null=False, default=0)

    class Meta:
        db_table = 'user_info'


class BLOG(models.Model):

    # 博客的唯一标识符
    blog_id = models.IntegerField(name='b_id', verbose_name='博客id', null=False, primary_key=False)
    # 博客的标题,最大长度为30
    blog_title = models.CharField(max_length=30, name='b_t', verbose_name='博客标题', null=False)
    # 博客的内容,最大长度为5000
    blog_content = models.CharField(max_length=5000, name='b_c', verbose_name='博客内容', null=False)
    # 用户id,对应用户表里的uid
    u_id = models.IntegerField(name='u_id',verbose_name='用户id',null=False)
    # 博客的类别 默认为0 临时不存在对应关系
    type_id = models.IntegerField(name='t_id',verbose_name='类别id',null=False,default=0)
    # 博客状态,0->正常 1 -> 删除 2 -> 违规
    blog_status = models.IntegerField(name='b_s',verbose_name='博客状态',null=False,default=0)
    # 发表时间格式为 YYYY/MM/DD HH/MM/SS
    createtime = models.DateTimeField(name='c_t', verbose_name='博客发布时间', null=False)
    # 修改时间
    updateTime = models.DateTimeField(name='u_t', verbose_name='博客修改时间', null=True)
    # 博客相关图片,多张已字符串方式拼接
    cover_image = models.CharField(max_length=1000,name='c_i',verbose_name='博客相关图片')

    class Meta:
        db_table = 't_blog'


class SCHOOL(models.Model):


    sn = models.CharField(max_length=20,name='schoolname',verbose_name='学校名称')

    class Meta():
        db_table = 'schools_table'