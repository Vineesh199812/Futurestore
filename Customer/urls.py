from django.urls import path
from Customer import views

urlpatterns=[
    path("",views.LoginView.as_view(),name="login"),
    path("register",views.RegistrationView.as_view(),name="registration"),
    path("home",views.HomeView.as_view(),name="home"),
    path("products/int:id",views.ProductDetailView.as_view(),name='product-detail')
]