from blog import views
from django.urls import path


# HTTP Request <-> HTTP Response
# MVT (MVC)

urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
]
