from django.urls import path
from . import views

app_name = "companies"

urlpatterns = [
    path("<int:pk>/", views.company_detail, name="company_detail"),
    path("<int:pk>/item_filtering/", views.item_filtering, name="item_filtering"),
]
