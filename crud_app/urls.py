from django.urls import path
from crud_app.views import home, add_book, delete_book, update_book

app_name = 'crudApp'

urlpatterns = [
    path("", home, name="home"),
    path("add_book/", add_book, name="add-book"),
    path("delete_book/<int:id>/", delete_book, name="delete_book"),
    path("update_book/<int:id>/", update_book, name="update_book"),
]