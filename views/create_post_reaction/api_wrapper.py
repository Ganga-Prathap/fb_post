from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from fb_post.utils.react_to_post import react_to_post
from fb_post.constants.exception_message import (
    INVALID_REACTION_TYPE,
    INVALID_POST_ID
)
from django_swagger_utils.drf_server.exceptions import (
    BadRequest,
    NotFound
)
from fb_post.exceptions import (
    InvalidPostException,
    InvalidReactionTypeException
)


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    post_id = kwargs['post_id']
    user = kwargs['user']
    request_data = kwargs['request_data']
    reaction_type=request_data['reaction_type']
    try:
        react_to_post(
            user_id=user.id,
            post_id=post_id,
            reaction_type=reaction_type
        )
    except InvalidPostException:
        raise NotFound(*INVALID_POST_ID)
    except InvalidReactionTypeException:
        raise BadRequest(*INVALID_REACTION_TYPE)
    return HttpResponse(status=200)


    """
    try:
        from fb_post.views.create_post_reaction.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from fb_post.views.create_post_reaction.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from fb_post.views.create_post_reaction.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="fb_post", test_case=test_case,
        operation_name="create_post_reaction",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """