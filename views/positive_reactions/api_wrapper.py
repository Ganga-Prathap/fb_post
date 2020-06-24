from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from fb_post.utils.get_posts_with_more_positive_reactions import (
    get_posts_with_more_positive_reactions
)


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    posts = get_posts_with_more_positive_reactions()

    data = json.dumps(posts)
    return HttpResponse(data, status=200)

    """
    try:
        from fb_post.views.positive_reactions.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from fb_post.views.positive_reactions.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from fb_post.views.positive_reactions.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="fb_post", test_case=test_case,
        operation_name="positive_reactions",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """