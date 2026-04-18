from django.urls import path,include
from skapp.Api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter() 
router.register('crude', views.Userview, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
