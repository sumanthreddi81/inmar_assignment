from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import LocationViewSet, DepartmentListCreateView, CategoryListCreateView, SubCategoryListCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'api/v1/location', LocationViewSet, basename='location')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/location/<int:location_id>/department/', DepartmentListCreateView.as_view(), name='location-departments'),
    path('api/v1/location/<int:location_id>/department/<int:department_id>/category/', CategoryListCreateView.as_view(), name='department-categories'),
    path('api/v1/location/<int:location_id>/department/<int:department_id>/category/<int:category_id>/subcategory/', SubCategoryListCreateView.as_view(), name='category-subcategories'),
]
