from django.conf.urls import url

from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("hello-vieset", views.helloViewSet, base_name="hello-viewset")

urlpatterns = [
    url(r'^hello-view/', views.helloApiView.as_view()),
    url(r'', include(router.urls))
]
