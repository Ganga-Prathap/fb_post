# pylint: disable=wrong-import-position

APP_NAME = "fb_post"
OPERATION_NAME = "reactions_metrics"
REQUEST_METHOD = "get"
URL_SUFFIX = "posts/{post_id}/reactions/metrics/v1/"

from .test_case_01 import TestCase01ReactionsMetricsAPITestCase

__all__ = [
    "TestCase01ReactionsMetricsAPITestCase"
]
