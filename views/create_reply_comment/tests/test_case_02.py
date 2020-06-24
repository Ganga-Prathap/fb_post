"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from fb_post.custom_utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from fb_post.factories.factories import PostFactory, CommentFactory

REQUEST_BODY = """
{
    "content": "string"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {"comment_id": "1"},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read", "write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02CreateReplyCommentAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase02CreateReplyCommentAPITestCase, self).setupUser(
            username=username, password=password
        )
        post = PostFactory.create()
        CommentFactory.create(post=post)

    def test_case(self):
        response = self.default_test_case() 

        import json
        from fb_post.models.comment import Comment

        response_content = json.loads(response.content)

        comment_id = response_content['comment_id']

        comment = Comment.objects.get(id=comment_id)

        self.assert_match_snapshot(
            name='user_id',
            value=comment.commented_by_id
        )
        self.assert_match_snapshot(
            name='post_id',
            value=comment.post_id
        )
        self.assert_match_snapshot(
            name='comment_id',
            value=comment.parent_comment_id
        )
        self.assert_match_snapshot(
            name='comment_content',
            value=comment.content
        )
