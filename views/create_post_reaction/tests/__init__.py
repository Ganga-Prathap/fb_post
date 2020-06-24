# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "create_post_reaction"
REQUEST_METHOD = "post"
URL_SUFFIX = "posts/{post_id}/react/v1/"

from .test_case_01 import TestCase01CreatePostReactionAPITestCase

__all__ = [
    "TestCase01CreatePostReactionAPITestCase"
]
