# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "create_comment_reaction"
REQUEST_METHOD = "post"
URL_SUFFIX = "comments/{comment_id}/react/v1/"

from .test_case_01 import TestCase01CreateCommentReactionAPITestCase

__all__ = [
    "TestCase01CreateCommentReactionAPITestCase"
]
