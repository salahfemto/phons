from django.db import models

# Create your models here.


class cate(models.Model):
    catname = models.CharField(max_length=30)

    def __str__(self):
        return self.catname


type_n = (
    ('pub', 'public'),
    ('pri', 'private'),
)


class numbers(models.Model):
    phone_n = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    n_type = models.CharField(max_length=10, choices=type_n)
    cat = models.ForeignKey(cate, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
