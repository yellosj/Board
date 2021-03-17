from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'), #list get
    path('post/<int:id>', views.detail, name='detail'), #post get
    #path('post/delete/<int:id>', views.delete, name='delete'), #삭제
    #path('post/edit/<int:id>', views.edit, name='edit'), #수정get
    #path('post/edit/update/<int:id>', views.update, name='update'), #수정post
    #일단 이 urls.py 부터 구조가 싹 달라지게 되는데,
    #거의 이렇게 다 사라지고 저거 하나만 사용해야 rest 고
    #저기 삭제, 수정(get,post) 다 없어지고 post/id 이거 하나만 사용하고 지금처럼 함수로 바로 이동시키는게 아니라 class로 이동을 시킨다음에
]
