from oscar.apps.catalogue.categories import create_from_breadcrumbs

categories = [
    "Headlights & Lighting > Turn Signals",
    "Headlights & Lighting > Fog Lights",
    "Headlights & Lighting > Headlights > Lights",
    "Interial Parts > Floor Mats",
    "Interial Parts > Gauges",
    "Interial Parts > Steering wheels",
    "Interial Parts > Cargo Accessories",
    "Repair Manual",
    "Fuel System",
]

for breadcrums in categories:
    create_from_breadcrumbs(breadcrums)


print("DONE CREATNG CATEGORIES")
