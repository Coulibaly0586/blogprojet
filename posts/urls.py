from django.urls import path
from posts.views import indexHome, indexCreate, indexUpdate, indexDelete, indexDetail

urlpatterns = [
    path('', indexHome.as_view(), name="home"),
    path('create/', indexCreate.as_view(), name="Create"),
    path('update/<int:pk>/', indexUpdate.as_view(), name="update"),
    path('Delete/<int:pk>/', indexDelete.as_view(), name="Delete"),
    path('Detail/<int:pk>/', indexDetail.as_view(), name="Detail"),
]
