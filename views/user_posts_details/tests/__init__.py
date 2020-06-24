# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "user_posts_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "users/posts/v1/"

from .test_case_01 import TestCase01UserPostsDetailsAPITestCase

__all__ = [
    "TestCase01UserPostsDetailsAPITestCase"
]
