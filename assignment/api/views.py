from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Location, Department, Category, SubCategory
from .serializers import LocationSerializer, DepartmentSerializer, CategorySerializer, SubCategorySerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]

class DepartmentListCreateView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Department.objects.filter(location_id=self.kwargs['location_id'])

    def perform_create(self, serializer):
        location = Location.objects.get(id=self.kwargs['location_id'])
        serializer.save(location=location)

class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(department_id=self.kwargs['department_id'])

    def perform_create(self, serializer):
        department = Department.objects.get(id=self.kwargs['department_id'])
        serializer.save(department=department)

class SubCategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SubCategory.objects.filter(category_id=self.kwargs['category_id'])

    def perform_create(self, serializer):
        category = Category.objects.get(id=self.kwargs['category_id'])
        serializer.save(category=category)
