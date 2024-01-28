from django.db import models


class UserData(models.Model):

    fruit_select = [
        ('apple', 'Apple'),
        ('banana', 'Banana'),
        ('orange', 'Orange'),
        ('grapes', 'Grape'),
        ('pineapple', 'Pineapple'),
        ('watermelon', 'Watermelon'),
        ('lychee', 'Lychee'),
        ('mango', 'Mango')
    ]

    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phoneNo = models.IntegerField()
    fruit_selection = models.CharField(max_length=100, choices=fruit_select)

    def __str__(self):
        return self.name


class FruitData(models.Model):
    fruitName = models.CharField(max_length=50)

    def __str__(self):
        return self.fruitName
