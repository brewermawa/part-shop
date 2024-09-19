from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractCategory, AbstractProduct


class Category(AbstractCategory):
    def get_cat_num_products(cat, count=0):
        if cat.has_children():
            for c in cat.get_children():
                count += c.get_cat_num_products()
        else:       
            return ProductCategory.objects.filter(category=cat).count()
        
        count += ProductCategory.objects.filter(category=cat).count()

        return count
            
    def get_num_products(self):
        return self.get_cat_num_products()
    

class Product(AbstractProduct):
    COLOR_CHOICES = [
        ("grn", "Green"),
        ("gry", "Grey"),
        ("blu", "Blue"),
        ("blk", "Black"),
        ("yel", "Yellow"),
        ("red", "Red"),
        ("wht", "White"),
    ]

    color = models.CharField(max_length=3, choices=COLOR_CHOICES, default="wht")


from oscar.apps.catalogue.models import * 
