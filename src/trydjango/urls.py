"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path # You have to manually import 'include' to add other apps urls.py

from pages.views import home_view, contact_view, about_view # Professional way of importing views function. The pages/ app handles the rendering of most HTML pages in this project.


urlpatterns = [
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    # Remember we are dedicating pages/ and products/ for two different purposes. Separate their urls path and import products/urls.py into this urls.py. Modularity!
    path('products/', include('products.urls')), # To look at all HTML templates in 'products/' check 'products/urls.py to understand products/views.py path. Check 'products/views.py' also to see comments of where the path is if you don't understand. 
    path('', home_view, name='home'), #E.g. http://127.0.0.1:8000/
    path('about/<int:id>/', about_view, name='product-detail'),
    path('contact/', contact_view), # E.g. http://127.0.0.1:8000/contacts
    path('admin/', admin.site.urls), # This is th url path to Admin page. Comment or delete this line and the Admin page is no longer accessable. It will still work though.
]


