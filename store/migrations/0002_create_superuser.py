from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='antonio').exists():
        User.objects.create(
            username='antonio',
            email='antonio@example.com',
            password=make_password('Antonio12345'),
            is_superuser=True,
            is_staff=True,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
