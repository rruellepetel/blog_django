from django.conf.urls import url, include
from views import homepage, post_list, post_detail,post_create,post_edit,post_delete


urlpatterns = [
    url(r'^$', homepage),
    url(r'^post/list$', post_list, name="post-list"),
    url(r'^post/create$', post_create, name="post-create"),
    url(r'^post/(?P<slug>[\w-]+)/edit$', post_edit, name="post-edit"),
    url(r'^post/(?P<slug>[\w-]+)/delete$', post_delete, name="post-delete"),
    url(r'^post/(?P<slug>[\w-]+)', post_detail, name="post-detail")
]
