"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from article import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/',views.Article_List,name='Article_List'),
    path('article_detail/<int:id>/',views.Article_detail,name='Article_detail'),
    path('article_create/',views.Article_create,name='Article_create'),
    path('article_delete/<int:id>/',views.Article_delete,name='Article_delete'),
    path('article_safe_delete/<int:id>/',views.Article_safe_delete,name='Article_safe_delete'),
    path('article_update/<int:id>/',views.Article_update,name='Article_update'),
    path('control/',include('control.urls',namespace='control')),
    path('password_reset/',include('password_reset.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)