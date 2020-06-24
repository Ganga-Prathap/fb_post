from django.conf.urls import url

from fb_post.build.view_environments.posts_v1_.router import posts_v1_
from fb_post.build.view_environments.posts__post_id__comment_v1_.router import posts__post_id__comment_v1_
from fb_post.build.view_environments.comments__comment_id__reply_v1_.router import comments__comment_id__reply_v1_
from fb_post.build.view_environments.posts__post_id__react_v1_.router import posts__post_id__react_v1_
from fb_post.build.view_environments.comments__comment_id__react_v1_.router import comments__comment_id__react_v1_
from fb_post.build.view_environments.posts__post_id__delete_v1_.router import posts__post_id__delete_v1_
from fb_post.build.view_environments.posts__post_id__details_v1_.router import posts__post_id__details_v1_
from fb_post.build.view_environments.users_posts_v1_.router import users_posts_v1_
from fb_post.build.view_environments.users_react_posts_v1_.router import users_react_posts_v1_
from fb_post.build.view_environments.reactions_count_v1_.router import reactions_count_v1_
from fb_post.build.view_environments.posts__post_id__reactions_metrics_v1_.router import posts__post_id__reactions_metrics_v1_
from fb_post.build.view_environments.posts__post_id__reactions_v1_.router import posts__post_id__reactions_v1_
from fb_post.build.view_environments.comments__comment_id__replies_v1_.router import comments__comment_id__replies_v1_
from fb_post.build.view_environments.posts_positive_reactions_v1_.router import posts_positive_reactions_v1_


urlpatterns = [
    url(r'^posts/v1/$', posts_v1_),
    url(r'^posts/(?P<post_id>\d+)/comment/v1/$', posts__post_id__comment_v1_),
    url(r'^comments/(?P<comment_id>\d+)/reply/v1/$', comments__comment_id__reply_v1_),
    url(r'^posts/(?P<post_id>\d+)/react/v1/$', posts__post_id__react_v1_),
    url(r'^comments/(?P<comment_id>\d+)/react/v1/$', comments__comment_id__react_v1_),
    url(r'^posts/(?P<post_id>\d+)/delete/v1/$', posts__post_id__delete_v1_),
    url(r'^posts/(?P<post_id>\d+)/details/v1/$', posts__post_id__details_v1_),
    url(r'^users/posts/v1/$', users_posts_v1_),
    url(r'^users/react/posts/v1/$', users_react_posts_v1_),
    url(r'^reactions/count/v1/$', reactions_count_v1_),
    url(r'^posts/(?P<post_id>\d+)/reactions/metrics/v1/$', posts__post_id__reactions_metrics_v1_),
    url(r'^posts/(?P<post_id>\d+)/reactions/v1/$', posts__post_id__reactions_v1_),
    url(r'^comments/(?P<comment_id>\d+)/replies/v1/$', comments__comment_id__replies_v1_),
    url(r'^posts/positive/reactions/v1/$', posts_positive_reactions_v1_),
]
