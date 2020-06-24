from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from fb_post.utils.get_reaction_metrics import (
    get_reaction_metrics
)
from fb_post.constants.exception_message import INVALID_POST_ID
from django_swagger_utils.drf_server.exceptions import NotFound
from fb_post.exceptions import InvalidPostException


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------
    post_id = kwargs['post_id']
    try:
        reaction_metrics = get_reaction_metrics(
            post_id=post_id
            )
    except InvalidPostException:
        raise NotFound(*INVALID_POST_ID)
    else:
        data = json.dumps(reaction_metrics)
        response = HttpResponse(data, status=200)
        return response

    """
    try:
        from fb_post.views.reactions_metrics.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from fb_post.views.reactions_metrics.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from fb_post.views.reactions_metrics.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="fb_post", test_case=test_case,
        operation_name="reactions_metrics",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """