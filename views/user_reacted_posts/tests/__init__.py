# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "user_reacted_posts"
REQUEST_METHOD = "get"
URL_SUFFIX = "users/react/posts/v1/"

from .test_case_01 import TestCase01UserReactedPostsAPITestCase

__all__ = [
    "TestCase01UserReactedPostsAPITestCase"
]
