
from django.urls import path
from .views import article_list, article_details
urlpatterns = [

    path("article/", article_list),
    path("details/<int:pk>/", article_details),
]
