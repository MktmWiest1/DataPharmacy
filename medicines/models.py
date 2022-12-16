from django.db import models


class Category(models.Model):
    image = models.ImageField(upload_to="media/")
    category_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category_name


class Medicine(models.Model):
    image = models.ImageField(upload_to="media/")
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


