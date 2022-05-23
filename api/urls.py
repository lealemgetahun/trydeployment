from django.urls.conf import path, include
from rest_framework import routers
from .views import ClassifyImage
# from django.urls import url 

app_name = 'product'
# router = routers.DefaultRouter()
# router.register('classify', views.ClassifyViewSet)
# router.register('api/post', views.tutorial_list)

urlpatterns = [
    # path('classify/', include(router.urls)),
    path('imageClassify/', ClassifyImage.as_view()),
    # path('api/post/', Classify, name = "classify")
]