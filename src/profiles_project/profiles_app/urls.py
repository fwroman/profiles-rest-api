from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hello-view/', views.helloApiView.as_view())
]
