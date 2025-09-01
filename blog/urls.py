from blog import views
from django.urls import path

app_name = 'blog'


# HTTP Request <-> HTTP Response
# MVT (MVC)

urlpatterns = [
    path('', views.blog, name='home'),
    path('exemplo1/', views.exemplo, name='exemplo'),
]
