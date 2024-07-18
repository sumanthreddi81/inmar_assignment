from rest_framework import serializers
from .models import Location, Department, Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'description']
        extra_kwargs = {'id': {'read_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'description', 'subcategories']
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        subcategories_data = validated_data.pop('subcategories')
        category = Category.objects.create(**validated_data)
        for subcategory_data in subcategories_data:
            SubCategory.objects.create(category=category, **subcategory_data)
        return category

    def update(self, instance, validated_data):
        subcategories_data = validated_data.pop('subcategories')
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        for subcategory_data in subcategories_data:
            subcategory_id = subcategory_data.get('id')
            if subcategory_id:
                subcategory = SubCategory.objects.get(id=subcategory_id, category=instance)
                subcategory.description = subcategory_data.get('description', subcategory.description)
                subcategory.save()
            else:
                SubCategory.objects.create(category=instance, **subcategory_data)

        return instance


class DepartmentSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Department
        fields = ['id', 'description', 'categories']
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        department = Department.objects.create(**validated_data)
        for category_data in categories_data:
            subcategories_data = category_data.pop('subcategories')
            category = Category.objects.create(department=department, **category_data)
            for subcategory_data in subcategories_data:
                SubCategory.objects.create(category=category, **subcategory_data)
        return department

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories')
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        for category_data in categories_data:
            subcategories_data = category_data.pop('subcategories')
            category_id = category_data.get('id')
            if category_id:
                category = Category.objects.get(id=category_id, department=instance)
                category.description = category_data.get('description', category.description)
                category.save()
            else:
                category = Category.objects.create(department=instance, **category_data)

            for subcategory_data in subcategories_data:
                subcategory_id = subcategory_data.get('id')
                if subcategory_id:
                    subcategory = SubCategory.objects.get(id=subcategory_id, category=category)
                    subcategory.description = subcategory_data.get('description', subcategory.description)
                    subcategory.save()
                else:
                    SubCategory.objects.create(category=category, **subcategory_data)

        return instance


class LocationSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True)

    class Meta:
        model = Location
        fields = ['id', 'description', 'departments']
        extra_kwargs = {'id': {'read_only': True}}

    def create(self, validated_data):
        departments_data = validated_data.pop('departments')
        location = Location.objects.create(**validated_data)
        for department_data in departments_data:
            categories_data = department_data.pop('categories')
            department = Department.objects.create(location=location, **department_data)
            for category_data in categories_data:
                subcategories_data = category_data.pop('subcategories')
                category = Category.objects.create(department=department, **category_data)
                for subcategory_data in subcategories_data:
                    SubCategory.objects.create(category=category, **subcategory_data)
        return location

    def update(self, instance, validated_data):
        departments_data = validated_data.pop('departments', None)

        instance.description = validated_data.get('description', instance.description)
        instance.save()

        if departments_data:
            for department_data in departments_data:
                categories_data = department_data.pop('categories', None)
                department_id = department_data.get('id')
                if department_id:
                    department = Department.objects.get(id=department_id, location=instance)
                    department.description = department_data.get('description', department.description)
                    department.save()
                else:
                    department = Department.objects.create(location=instance, **department_data)

                if categories_data:
                    for category_data in categories_data:
                        subcategories_data = category_data.pop('subcategories', None)
                        category_id = category_data.get('id')
                        if category_id:
                            category = Category.objects.get(id=category_id, department=department)
                            category.description = category_data.get('description', category.description)
                            category.save()
                        else:
                            category = Category.objects.create(department=department, **category_data)

                        if subcategories_data:
                            for subcategory_data in subcategories_data:
                                subcategory_id = subcategory_data.get('id')
                                if subcategory_id:
                                    subcategory = SubCategory.objects.get(id=subcategory_id, category=category)
                                    subcategory.description = subcategory_data.get('description',
                                                                                   subcategory.description)
                                    subcategory.save()
                                else:
                                    SubCategory.objects.create(category=category, **subcategory_data)
        return instance
