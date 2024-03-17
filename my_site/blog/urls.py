from django.urls import path
from . import views


urlpatterns = [
    path("", views.startingpage, name='starting-page'),
    path("posts/",views.posts, name='posts-page'),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]

