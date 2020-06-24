from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from fb_post.utils.get_total_reaction_count import (
    get_total_reaction_count
)

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    reactions_count = get_total_reaction_count()

    data = json.dumps(reactions_count)
    return HttpResponse(data, status=200)

    """
    try:
        from fb_post.views.reactions_count.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from fb_post.views.reactions_count.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from fb_post.views.reactions_count.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="fb_post", test_case=test_case,
        operation_name="reactions_count",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """