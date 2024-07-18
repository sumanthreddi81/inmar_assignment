from api.models import Location, Department, Category, SubCategory

def populate_metadata():
    # Data to be populated
    metadata = [
        ("Perimeter", "Bakery", "Bakery Bread", "Bagels"),
        ("Perimeter", "Bakery", "Bakery Bread", "Baking or Breading Products"),
        ("Perimeter", "Bakery", "Bakery Bread", "English Muffins or Biscuits"),
        ("Perimeter", "Bakery", "Bakery Bread", "Flatbreads"),
        ("Perimeter", "Bakery", "In Store Bakery", "Breakfast Cake or Sweet Roll"),
        ("Perimeter", "Bakery", "In Store Bakery", "Cakes"),
        ("Perimeter", "Bakery", "In Store Bakery", "Pies"),
        ("Perimeter", "Bakery", "In Store Bakery", "Seasonal"),
        ("Center", "Dairy", "Cheese", "Cheese Sauce"),
        ("Center", "Dairy", "Cheese", "Specialty Cheese"),
        ("Center", "Dairy", "Cream or Creamer", "Dairy Alternative Creamer"),
        ("Center", "Frozen", "Frozen Bake", "Bread or Dough Products Frozen"),
        ("Center", "Frozen", "Frozen Bake", "Breakfast Cake or Sweet Roll Frozen"),
    ]

    # Create locations, departments, categories, and subcategories
    for location_name, department_name, category_name, subcategory_name in metadata:
        location, _ = Location.objects.get_or_create(description=location_name)
        department, _ = Department.objects.get_or_create(description=department_name, location=location)
        category, _ = Category.objects.get_or_create(description=category_name, department=department)
        SubCategory.objects.get_or_create(description=subcategory_name, category=category)

populate_metadata()
