from django.db import models

class Location(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Department(models.Model):
    location = models.ForeignKey(Location, related_name='departments', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Category(models.Model):
    department = models.ForeignKey(Department, related_name='categories', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
