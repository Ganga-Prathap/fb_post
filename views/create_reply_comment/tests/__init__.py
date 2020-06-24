# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "create_reply_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "comments/{comment_id}/reply/v1/"

from .test_case_01 import TestCase01CreateReplyCommentAPITestCase

__all__ = [
    "TestCase01CreateReplyCommentAPITestCase"
]
