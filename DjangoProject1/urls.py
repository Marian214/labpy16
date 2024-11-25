
from django.contrib import admin
# from django.urls import path
# from app_blog import views
#
# urlpatterns = [
#     path('', views.HomePageView.as_view(), name='home'),
# ]
# """"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]