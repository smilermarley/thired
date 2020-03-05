from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?p<pk>\d+)$'),views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',Views.CreateView.as_view(),name='post_new'),
    url(r'^post/(?p<pk>\d+)/edit/$',Views.PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?p<pk>\d+)/remove/$',Viws.PostDeleteView.as_view(),name='post_remove'),
    url(r'^drafts/$',Views.DraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?p<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),
    url(r'^comment/(?p<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?p<pk>\d+)/remove/$',views.comment_remove,name='comment_remove'),
    url(r'^post/(?p<pk>\d+)/publish/$',views.post_publish,name='post_publish'),

]
