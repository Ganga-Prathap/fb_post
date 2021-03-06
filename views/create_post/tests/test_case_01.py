"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "content": "string"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01CreatePostAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CreatePostAPITestCase, self).setupUser(
            username=username, password=password
        )

    def test_case(self):
        response = self.default_test_case() 

        import json
        from fb_post.models.post import Post

        response_content = json.loads(response.content)
        post_id = response_content['post_id']
        post = Post.objects.select_related('posted_by').get(id=post_id)

        self.assert_match_snapshot(
            name='user_id',
            value=post.posted_by_id
        )
        self.assert_match_snapshot(
            name='post_content',
            value=post.content
        )
