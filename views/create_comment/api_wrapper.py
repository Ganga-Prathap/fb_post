from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass
from fb_post.utils.create_comment import create_comment
from fb_post.constants.exception_message import (
    INVALID_COMMENT_CONTENT,
    INVALID_POST_ID
)
from django_swagger_utils.drf_server.exceptions import (
    BadRequest,
    NotFound
)
from fb_post.exceptions import (
    InvalidPostException,
    InvalidCommentContent
)


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    post_id = kwargs['post_id']
    user = kwargs['user']
    request_data = kwargs['request_data']
    comment_content=request_data['content']
    try:
        comment_id = create_comment(
        user_id=user.id,
        post_id=post_id,
        comment_content=comment_content
        )
    except InvalidPostException:
        raise NotFound(*INVALID_POST_ID)
    except InvalidCommentContent:
        raise BadRequest(*INVALID_COMMENT_CONTENT)
    else:
        data = json.dumps({"comment_id": comment_id})
        response = HttpResponse(data, status=201)
        return response

    """
    try:
        from fb_post.views.create_comment.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from fb_post.views.create_comment.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from fb_post.views.create_comment.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="fb_post", test_case=test_case,
        operation_name="create_comment",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """
