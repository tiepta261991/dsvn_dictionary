from django.conf.urls import url 
from dsvn_dictionary import views 
from django.urls import path
from .views import UserRegisterView, UserLoginView, ViSpeechGooleView, JaSpeechGooleView

urlpatterns = [ 
    # http://127.0.0.1:8000/api/vidictionary :get list vi-dic all or add new word or delete all 
    url(r'^api/vidictionary$', views.vidictionary_list),
    # http://127.0.0.1:8000/api/search/vidictionary?vi_text=giao vien : search by viet name word to japan word
    url(r'^api/search/vidictionary$', views.vidictionary_search),
    # http://127.0.0.1:8000/api/update/jadictionary/$id: update row vi-dic by id
    url(r'^api/update/vidictionary/(?P<pk>[0-9]+)$', views.vidictionary_update),
    # http://127.0.0.1:8000/api/delete/jadictionary/$id : delete row by id
    url(r'^api/delete/vidictionary/(?P<pk>[0-9]+)$', views.vidictionary_delete),
    # http://127.0.0.1:8000/api/jadictionary :get list vi-dic all or add new word or delete all 
    url(r'^api/jadictionary$', views.jadictionary_list),
    # http://127.0.0.1:8000/api/search/jadictionary?ja_text=会議室 : search by japan word to viet nam word
    url(r'^api/search/jadictionary$', views.jadictionary_search),
    # http://127.0.0.1:8000/api/update/jadictionary/1 : update row ja-dic by id
    url(r'^api/update/jadictionary/(?P<pk>[0-9]+)$', views.jadictionary_update),
    # http://127.0.0.1:8000/api/delete/jadictionary/2 : delete row by id
    url(r'^api/delete/jadictionary/(?P<pk>[0-9]+)$', views.jadictionary_delete),

    path('admin/register', UserRegisterView.as_view(), name='register'),
    path('admin/login', UserLoginView.as_view(), name='login'),

    path('api/vi/speech', ViSpeechGooleView.as_view(), name='info'),
    path('api/ja/speech', JaSpeechGooleView.as_view(), name='info'),
]