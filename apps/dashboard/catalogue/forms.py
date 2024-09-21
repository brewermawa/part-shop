from oscar.apps.dashboard.catalogue import forms as base_forms
from oscar.core.loading import get_model

Product = get_model("catalogue", "Product")

class ProductForm(base_forms.ProductForm):
    class Meta(base_forms.ProductForm):
        model = Product
        fields = [
            "title",
            "upc",
            "color",
            "description",
            "is_public",
            "is_discountable",
            "structure",
            "slug",
            "meta_title",
            "meta_description",
        ]