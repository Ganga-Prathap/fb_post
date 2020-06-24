path_method_dict = {
    "posts/positive/reactions/v1/": {
        "GET": "positive_reactions"
    }
}


def posts_positive_reactions_v1_(request, *args, **kwargs):
    from django_swagger_utils.drf_server.utils.server_gen.get_operations_dict import get_operations_dict
    operations_dict = get_operations_dict(path_method_dict, request.path)

    from django_swagger_utils.drf_server.wrappers.router_wrapper import router_wrapper
    response = router_wrapper("fb_post", "posts_positive_reactions_v1_", operations_dict, request, *args, **kwargs)
    return response