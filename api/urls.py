from django.urls import path
from api.views import CategoriesView,ProductsView
from rest_framework.routers import DefaultRouter
from api import views

router=DefaultRouter()
router.register("categories",views.CategoriesView,basename="categories")
router.register("products",views.ProductsView,basename="products")
# router.register("categories/<int:id>/products",views.ProductsView,basename="products-list")

urlpatterns=[
    # path("categories/<int:id>/products",views.ProductsView.as_view())
]+router.urls