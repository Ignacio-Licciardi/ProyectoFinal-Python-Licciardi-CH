from django.urls import path

from .views import CreateBlog , ListBlog , UpdateBlog , DeleteBlog , DetailBlog


urlpatterns = [
    path("post/", CreateBlog.as_view(), name="create_blog"),
    path("list_blog/", ListBlog.as_view(), name="list_blog"),
    path("edit/<pk>", UpdateBlog.as_view(), name="update_blog"),
    path("delete/<pk>", DeleteBlog.as_view(), name="delete_blog"),
    path('blog/<int:pk>/detail', DetailBlog.as_view(), name='detail_blog'),
]
