from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass
from fb_post.utils.reply_to_comment import reply_to_comment
from fb_post.constants.exception_message import (
    INVALID_REPLY_CONTENT,
    INVALID_COMMENT_ID
)
from django_swagger_utils.drf_server.exceptions import (
    BadRequest,
    NotFound
)
from fb_post.exceptions import (
    InvalidCommentException,
    InvalidReplyContent
)


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    comment_id = kwargs['comment_id']
    user = kwargs['user']
    request_data = kwargs['request_data']
    comment_content=request_data['content']
    try:
        reply_comment_id = reply_to_comment(
        user_id=user.id,
        comment_id=comment_id,
        reply_content=comment_content
        )
    except InvalidCommentException:
        raise NotFound(*INVALID_COMMENT_ID)
    except InvalidReplyContent:
        raise BadRequest(*INVALID_REPLY_CONTENT)
    else:
        data = json.dumps({"comment_id": reply_comment_id})
        response = HttpResponse(data, status=201)
        return response

    """
    try:
        from fb_post.views.create_reply_comment.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from fb_post.views.create_reply_comment.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from fb_post.views.create_reply_comment.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="fb_post", test_case=test_case,
        operation_name="create_reply_comment",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """