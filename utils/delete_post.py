from .validations import (
    is_valid_user_id,
    is_valid_post_id,
    is_valid_user_to_delete_post
)


# Task-9
def delete_post(user_id, post_id):

    is_valid_user_id(user_id)

    post_obj = is_valid_post_id(post_id)

    is_valid_user_to_delete_post(post_obj, user_id)

    post_obj.delete()
