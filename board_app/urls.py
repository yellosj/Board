from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'), #list get
    path('post/<int:id>', views.detail, name='detail'), #post get
    path('post/delete/<int:id>', views.delete, name='delete'), #삭제
    path('post/edit/<int:id>', views.edit, name='edit'), #수정get
    path('post/edit/update/<int:id>', views.update, name='update'), #수정post

]
