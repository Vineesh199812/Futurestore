from django.urls import path
from Owner import views

urlpatterns=[
    path("index",views.AdminDashBoardView.as_view(),name="dashboard")
]