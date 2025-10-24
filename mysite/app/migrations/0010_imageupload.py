from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('img', models.FileField(upload_to='images/', verbose_name='图片')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
        ),
    ]

