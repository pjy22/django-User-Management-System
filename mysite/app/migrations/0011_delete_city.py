from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_imageupload'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
    ]
