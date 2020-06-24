from fb_post.models.comment import Comment
from .validations import is_valid_comment_id
from .conversion_function_utils import (
    get_response_time,
    get_user_details_dict
)


def get_reply_comment_dict_form(comment):

    reply_comment_dictionary = {
        'comment_id': comment.id,
        'commenter': get_user_details_dict(comment.commented_by),
        'commented_at': get_response_time(comment.commented_at),
        'comment_content': comment.content,
    }

    return reply_comment_dictionary

def get_replies_for_comment(comment_id):

    is_valid_comment_id(comment_id)

    reply_comment_objs = Comment.objects.select_related(
        'commented_by')\
        .filter(parent_comment_id=comment_id)

    comment_list = []

    for reply_comment_obj in reply_comment_objs:
        comment_list.append(get_reply_comment_dict_form(reply_comment_obj))

    return comment_list
