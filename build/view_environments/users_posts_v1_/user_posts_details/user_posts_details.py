from django_swagger_utils.drf_server.decorators.request_response import request_response
from django_swagger_utils.drf_server.default.parser_mapping import PARSER_MAPPING
from django_swagger_utils.drf_server.default.renderer_mapping import RENDERER_MAPPING
from fb_post.build.view_environments.users_posts_v1_.user_posts_details.UserPostsDetailsRequestQueryParamSerializer import UserPostsDetailsRequestQueryParamSerializer
from fb_post.build.responses.UserPostDetailResponse.UserPostDetailResponse.UserPostDetailResponseSerializer import UserPostDetailResponseSerializer


options = {
    'METHOD': 'GET',
    'REQUEST_WRAPPING_REQUIRED': False,
    'REQUEST_ENCRYPTION_REQUIRED': False,
    'REQUEST_IS_PARTIAL': False,
    'PARSER_CLASSES': [
        PARSER_MAPPING["application/json"]
    ],
    'RENDERER_CLASSES': [
        RENDERER_MAPPING["application/json"]
    ],
    'REQUEST_QUERY_PARAMS_SERIALIZER': UserPostsDetailsRequestQueryParamSerializer,
    'REQUEST_HEADERS_SERIALIZER': None,
    'REQUEST_SERIALIZER': None,
    'REQUEST_SERIALIZER_MANY_ITEMS': False,
    'RESPONSE': {
        
        '200' : {
           'RESPONSE_SERIALIZER': UserPostDetailResponseSerializer,
           'RESPONSE_SERIALIZER_MANY_ITEMS':  False,
           'HEADERS_SERIALIZER': None,
        }
        
    },
    "SECURITY":{

        "oauth" : [
            "superuser"
            
        ]
    }
}

app_name = "fb_post"
operation_id  = "user_posts_details"
group_name = ""

@request_response(options=options, app_name=app_name, operation_id=operation_id, group_name=group_name)
def user_posts_details(request, *args, **kwargs):
    args = (request,) + args
    from django_swagger_utils.drf_server.wrappers.view_env_wrapper import view_env_wrapper
    return view_env_wrapper(app_name, "user_posts_details", group_name, *args, **kwargs)
