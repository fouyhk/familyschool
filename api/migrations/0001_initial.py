# Generated by Django 3.2.16 on 2022-11-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BLOG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.IntegerField(verbose_name='博客id')),
                ('b_t', models.CharField(max_length=30, verbose_name='博客标题')),
                ('b_c', models.CharField(max_length=5000, verbose_name='博客内容')),
                ('u_id', models.IntegerField(verbose_name='用户id')),
                ('t_id', models.IntegerField(default=0, verbose_name='类别id')),
                ('b_s', models.IntegerField(default=0, verbose_name='博客状态')),
                ('c_t', models.DateTimeField(verbose_name='博客发布时间')),
                ('u_t', models.DateTimeField(null=True, verbose_name='博客修改时间')),
                ('c_i', models.CharField(max_length=1000, verbose_name='博客相关图片')),
            ],
            options={
                'db_table': 't_blog',
            },
        ),
        migrations.CreateModel(
            name='FUSER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.BigIntegerField(verbose_name='用户id')),
                ('open_id', models.CharField(max_length=30, verbose_name='用户openid')),
                ('u_nc', models.CharField(max_length=10, verbose_name='用户昵称')),
                ('t_x', models.CharField(max_length=200, verbose_name='用户头像')),
                ('c_t', models.DateTimeField(verbose_name='用户注册时间')),
                ('s_id', models.IntegerField(verbose_name='学校id')),
                ('a_g', models.IntegerField(verbose_name='用户协议同意情况')),
                ('u_st', models.IntegerField(default=0, verbose_name='用户签到积分')),
                ('u_sta', models.IntegerField(default=0, verbose_name='用户账号状态')),
                ('u_p', models.BigIntegerField(verbose_name='用户手机')),
                ('a_id', models.IntegerField(null=True, verbose_name='用户收货地址id')),
                ('u_t', models.DateTimeField(null=True, verbose_name='用户信息更新时间')),
                ('l_t', models.DateTimeField(verbose_name='用户最后一次登录时间')),
                ('u_s', models.IntegerField(default=0, verbose_name='用户性别')),
                ('u_r', models.IntegerField(default=0, verbose_name='用户等级')),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
    ]
