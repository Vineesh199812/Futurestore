from django.urls import path
from api.views import CategoriesView,ProductsView
from rest_framework.routers import DefaultRouter
from api.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView


router=DefaultRouter()
router.register("categories/post",CategoriesView,basename="categories")
router.register("products",ProductsView,basename="products")
router.register("carts",CartsView,basename="carts")
router.register("accounts/signup",UserRegistrationView,basename="registration")

urlpatterns=[
    path("token/",TokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    # path("accounts/token/",obtain_auth_token)
]+router.urls+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)