from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    # В файле models.py нашего приложения создаем модель Phone с полями
    # id, name, price, image, release_date, lte_exists и slug. Поле id - должно быть основным ключом модели.
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    lte_exists = models.BooleanField()
    slug = models.SlugField()

