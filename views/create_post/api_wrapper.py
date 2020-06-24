from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from .validator_class import ValidatorClass
from fb_post.utils.create_post import create_post
from fb_post.constants.exception_message import INVALID_POST_CONTENT
from django_swagger_utils.drf_server.exceptions import BadRequest
from fb_post.exceptions import InvalidPostContent


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs['user']
    request_data = kwargs['request_data']
    post_content=request_data['content']
    try:
        post_id = create_post(
            user_id=user.id,
            post_content=post_content
        )
    except InvalidPostContent:
        raise BadRequest(*INVALID_POST_CONTENT)
    else:
        data = json.dumps({"post_id": post_id})
        response = HttpResponse(data, status=201)
        return response
    

    """
    try:
        from fb_post.views.create_post.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from fb_post.views.create_post.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from fb_post.views.create_post.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="fb_post", test_case=test_case,
        operation_name="create_post",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """
