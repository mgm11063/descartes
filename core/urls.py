from django.urls import path
from companies import views as companies_views

app_name = "core"

urlpatterns = [
    path("", companies_views.index, name="home"),
]
