from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category_name


class Medicine(models.Model):
    image = models.ImageField(upload_to="media/")
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title



