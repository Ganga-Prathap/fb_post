from django.db.models import Prefetch
from fb_post.models.post import Post
from fb_post.models.comment import Comment
from .conversion_function_utils import get_post_dictionary
from .validations import is_valid_post_id


# Task-13
def get_post(post_id):

    is_valid_post_id(post_id)

    comment_queryset = Comment.objects.select_related('commented_by')\
                              .prefetch_related('reactions')
    post_obj = Post.objects.filter(id=post_id)\
                   .select_related('posted_by')\
                   .prefetch_related(
                       'reactions',
                       Prefetch('comments', queryset=comment_queryset)
                   ).get(id=post_id)

    post_dictionary = get_post_dictionary(post_obj)

    return post_dictionary
