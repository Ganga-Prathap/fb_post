# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "comment_replies"
REQUEST_METHOD = "get"
URL_SUFFIX = "comments/{comment_id}/replies/v1/"

from .test_case_01 import TestCase01CommentRepliesAPITestCase

__all__ = [
    "TestCase01CommentRepliesAPITestCase"
]
