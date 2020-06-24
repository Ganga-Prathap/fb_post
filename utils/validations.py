from fb_post.models.user import User
from fb_post.models.post import Post
from fb_post.models.comment import Comment
from fb_post.constants.reaction_enum import ReactionEnum
from fb_post.exceptions import (
    InvalidUserException,
    InvalidPostContent,
    InvalidCommentException,
    InvalidPostException,
    InvalidReactionTypeException,
    InvalidCommentContent,
    InvalidReplyContent,
    UserCannotDeletePostException
)


def is_valid_user_id(user_id):

    try:
        User.objects.get(id=user_id)

    except User.DoesNotExist:
        raise InvalidUserException


def is_valid_post_id(post_id):

    try:
        post_obj = Post.objects.get(id=post_id)
        return post_obj

    except Post.DoesNotExist:
        raise InvalidPostException

def is_valid_post_content(content):

    empty_content = not content

    if empty_content:
        raise InvalidPostContent

def is_valid_comment_id(comment_id):

    try:
        comment_obj = Comment.objects.get(id=comment_id)
        return comment_obj

    except Comment.DoesNotExist:
        raise InvalidCommentException

def is_valid_comment_content(content):

    empty_content = not content

    if empty_content:
        raise InvalidCommentContent

def is_valid_reply_content(content):

    empty_content = not content

    if empty_content:
        raise InvalidReplyContent

def is_valid_reaction_type(reaction_type):

    try:
        ReactionEnum(reaction_type)

    except ValueError:
        raise InvalidReactionTypeException


def is_valid_user_to_delete_post(post_obj, user_id):

    post_created_by_given_user = post_obj.posted_by_id != user_id

    if post_created_by_given_user:
        raise UserCannotDeletePostException
