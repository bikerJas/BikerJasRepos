from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.button),
    re_path(r'^external', views.external, name="script"),
]
