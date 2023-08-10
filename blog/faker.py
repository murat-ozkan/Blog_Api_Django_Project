from faker import Faker
from django.contrib.auth.models import User
from .models import Category, Post

def run():
    fake = Faker(['tr-TR'])
    categories = ('Travel', 'Food', 'Sports', 'Science')

    for category in categories:
        for x in range(50):
            Post.objects.create(
                title = fake.sentence(),
                content = fake.text(),
                category = Category.objects.create(name=category),
                user = User.objects.first()
            )

    print('Finished')