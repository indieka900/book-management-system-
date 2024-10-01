from django.urls import path
from crud_app.views import home, add_book, delete_book

app_name = 'crudApp'

urlpatterns = [
    path("", home, name="home"),
    path("add_book/", add_book, name="add-book"),
    path("delete_book/<id>/", delete_book, name="delete_book"),
]