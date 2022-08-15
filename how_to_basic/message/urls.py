from django.urls import path
from message.views import *

urlpatterns = [
    path('', MessagesList.as_view(), name="Messages"),
    path('new/', MessageCreate.as_view(), name="New_message"),
    path('<pk>/', MessageDetail.as_view(), name="Message_detail"),
    path('delete/<pk>', MessageDelete.as_view(), name="Delete_message"),
]
