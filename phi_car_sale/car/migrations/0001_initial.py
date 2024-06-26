
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
