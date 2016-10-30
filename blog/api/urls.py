from django.conf.urls import url
from blog.api import views

urlpatterns = [
    url(r'^', views.PostListView.as_view(), name='post_list_api'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$',views.post_new,name='post_new'),
    # url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    # url(r'^post/(?P<pk>\d+)/delete/$', views.post_remove, name='post_remove'),
    # url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),


]