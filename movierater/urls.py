
from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from movierater.api import views
from django.urls import path
from movierater.api.views import question

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('question/', question, name='square'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

