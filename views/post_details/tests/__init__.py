# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "post_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "posts/{post_id}/details/v1/"

from .test_case_01 import TestCase01PostDetailsAPITestCase

__all__ = [
    "TestCase01PostDetailsAPITestCase"
]
