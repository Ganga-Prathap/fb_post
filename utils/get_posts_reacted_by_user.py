from fb_post.models.post import Post
from .validations import is_valid_user_id

# Task-11
def get_posts_reacted_by_user(user_id):

    is_valid_user_id(user_id)

    user_reacted_post_ids = list(Post.objects.filter(
                reactions__reacted_by_id=user_id)\
                .values_list('id', flat=True))

    return user_reacted_post_ids
