# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "positive_reactions"
REQUEST_METHOD = "get"
URL_SUFFIX = "posts/positive/reactions/v1/"

from .test_case_01 import TestCase01PositiveReactionsAPITestCase

__all__ = [
    "TestCase01PositiveReactionsAPITestCase"
]
