from django.db.models import Prefetch
from fb_post.models.post import Post
from fb_post.models.comment import Comment
from .conversion_function_utils import get_post_dictionary
from .validations import is_valid_user_id


# Task-14
def get_user_posts(user_id, offset, limit):

    is_valid_user_id(user_id)

    comment_queryset = Comment.objects.select_related('commented_by')\
                              .prefetch_related('reactions')

    post_objs = Post.objects.filter(posted_by_id=user_id)\
                    .select_related('posted_by')\
                    .prefetch_related(
                        'reactions',
                        Prefetch('comments', queryset=comment_queryset))\
                        [offset:offset+limit]

    posts_list = [
        get_post_dictionary(post_obj)
        for post_obj in post_objs
    ]

    return posts_list
