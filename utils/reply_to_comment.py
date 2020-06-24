from fb_post.models.comment import Comment

from .validations import (
    is_valid_user_id,
    is_valid_comment_id,
    is_valid_reply_content
)


# Task-4
def reply_to_comment(user_id, comment_id, reply_content):

    is_valid_user_id(user_id)

    comment_obj = is_valid_comment_id(comment_id)

    is_valid_reply_content(reply_content)

    if comment_obj.parent_comment_id:
        parent_comment_id = comment_obj.parent_comment_id
    else:
        parent_comment_id = comment_id

    reply_comment_obj = Comment.objects.create(
        content=reply_content,
        commented_by_id=user_id,
        post_id=comment_obj.post_id,
        parent_comment_id=parent_comment_id
        )

    return reply_comment_obj.id
