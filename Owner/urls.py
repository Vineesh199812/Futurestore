from django.urls import path
from Owner import views


urlpatterns=[
    path("index",views.AdminDashBoardView.as_view(),name="dashboard"),
    path("orders/latest",views.OrdersListView.as_view(),name="neworders"),
    path("orders/details/<int:id>",views.OrderDetailView.as_view(),name="order-details"),
    path("products/all",views.ProductListView.as_view(),name="products-all"),
    path("signout", views.SignOutView.as_view(), name="signout")
]