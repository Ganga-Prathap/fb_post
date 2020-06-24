"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from fb_post.custom_utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "content": "string"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"post_id": "1234"},
        "query_params": {},
        "header_params": {},
        "securities": {
            "oauth": {
                "tokenUrl": "http://auth.ibtspl.com/oauth2/",
                "flow": "password",
                "scopes": [
                    "read",
                    "write"
                ],
                "type": "oauth2"
            }
        },
        "body": REQUEST_BODY,
    },
}


class TestCase01CreateCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CreateCommentAPITestCase, self).setupUser(
            username=username, password=password
        )
        print("1: \n")
        print("hello: ", self.foo_user)
        print("user_id: ", self.foo_user.id)
        print("\n2: \n")

    def test_case(self):
        self.default_test_case()
