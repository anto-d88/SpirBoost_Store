from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')

    username = "antonio"
    email = "antonio@example.com"
    password = "Antonio12345"

    if not User.objects.filter(username=username).exists():
        User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
            is_superuser=True,
            is_staff=True
        )
        print(">>> Superuser created ❤️")
    else:
        print(">>> Superuser already exists")


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
