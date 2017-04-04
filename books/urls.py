from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from books import views

urlpatterns = [
        url(r'^book/$', views.BookList.as_view(),
            name='book-list'),
        url(r'^author/$', views.AuthorList.as_view(),
            name='author-list'),
        url(r'^book/(?P<pk>[0-9]+)$', views.BookDetail.as_view(),
            name='book-detail'),
        url(r'^author/(?P<pk>[0-9]+)$', views.AuthorDetail.as_view(),
            name='author-detail'),
        ]
urlpatterns = format_suffix_patterns(urlpatterns)
