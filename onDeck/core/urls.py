from django.urls import include, path

from .views import (dashboard, login_page)

urlpatterns = [
    path("log-in", login_page, name="login"),
    path("", dashboard, name="dashboard"),
]
