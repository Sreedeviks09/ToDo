"""
URL configuration for TodoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin  # Importing the admin module to access the Django admin interface
from django.urls import path  # Importing the path function for URL routing
from TodoApp import views  # Importing the views from the TodoApp application

# Defining URL patterns for the application
urlpatterns = [
    # The 'admin/' path routes to the Django admin interface
    path('admin/', admin.site.urls),  # Admin URL pattern, accessible at 'http://localhost/admin/'

    # The home page route: Maps the root URL ('') to the Taskadd view
    path('', views.Taskadd, name='home'),  # The home route, where tasks are displayed and added

    # The delete page route: Maps 'delete/taskId' to the delete view, with a taskId parameter
    path('delete/<int:taskId>/', views.delete, name='delete'),  # Route to delete a task with the specified taskId

    # The update page route: Maps 'update/id' to the update view, with an id parameter
    path('update/<int:id>/', views.update, name='update')  # Route to update a task with the specified id
]

