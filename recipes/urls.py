from django.urls import path

from recipes.views import home

# domain/
urlpatterns = [
    path('', home),  # home
]
