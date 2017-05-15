from django.conf.urls import url, include
from views import homepage, post_list, post_detail


urlpatterns = [
    url(r'^$', homepage),
    url(r'^post/list$', post_list, name="post-list"),
    url(r'^post/(?P<slug>[\w-]+)', post_detail, name="post-detail")
]
