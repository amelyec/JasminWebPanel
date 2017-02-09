from django.conf.urls import url
from .views.login import login_view
from .views.dashboard import dashboard_view

urlpatterns = [
    url(r'^account/$', login_view, name='login_view'),
    url(r'^dashboard/$', dashboard_view, name='dashboard_view'),
]