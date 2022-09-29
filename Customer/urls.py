from django.urls import path
from Customer import views

urlpatterns=[
    path("",views.LoginView.as_view(),name="login"),
    path("register",views.RegistrationView.as_view(),name="registration"),
    path("home",views.HomeView.as_view(),name="home"),
    path("products/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path("products/<int:id>/carts/add",views.AddtoCartView.as_view(),name="addto-cart"),
    path("carts/all",views.MyCartView.as_view(),name="mycart"),
    # path("carts/remove/<int:id>",views.remove_product,name="remove-product"),
    path("carts/orders/<int:cid>/<int:pid>",views.PlaceOrderView.as_view(),name="place-order"),
    # path("carts/orders/")
]