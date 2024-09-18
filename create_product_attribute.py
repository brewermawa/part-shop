from oscar.apps.catalogue.models import *

material = AttributeOptionGroup.objects.create(name="material")
color = AttributeOptionGroup.objects.create(name="color")

AttributeOption.objects.create(
    group=material,
    option="Steel",
)

AttributeOption.objects.create(
    group=material,
    option="Aluminium",
)

AttributeOption.objects.create(
    group=material,
    option="Thorium",
)

AttributeOption.objects.create(
    group=color,
    option="Red",
)

AttributeOption.objects.create(
    group=color,
    option="Blue",
)

AttributeOption.objects.create(
    group=color,
    option="Black",
)

AttributeOption.objects.create(
    group=color,
    option="White",
)

print("DONE")
