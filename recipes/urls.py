from django.urls import path

from recipes.views import about, contact, home

# domain/
urlpatterns = [
    path('', home),  # home
    path('sobre/', about),  # /sobre/
    path('contato/', contact),  # /contato/
]
