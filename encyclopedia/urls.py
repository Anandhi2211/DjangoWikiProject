from django.urls import path

from . import views


app_name = "encylopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>",views.entrypage, name ="entrypage"),
    path("search/",views.search, name="search"),
    path("newpage/",views.newpage, name="newpage"),
    path("save/",views.save,name="save"),
    path("editpage/<str:title>",views.editpage,name="editpage"),
    path("editsave/",views.editsave,name="editsave"),
    path("randompage/",views.randompage,name="randompage")

]
