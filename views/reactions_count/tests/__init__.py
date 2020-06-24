# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "reactions_count"
REQUEST_METHOD = "get"
URL_SUFFIX = "reactions/count/v1/"

from .test_case_01 import TestCase01ReactionsCountAPITestCase

__all__ = [
    "TestCase01ReactionsCountAPITestCase"
]
