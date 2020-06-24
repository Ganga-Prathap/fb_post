class PostReactionsResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"user_id": 1, "name": "string", "profile_pic": "string", "reaction": "WOW"}]',
            "response_serializer": "PostReactionsResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.PostReactionsResponse.PostReactionsResponse.PostReactionsResponseSerializer import PostReactionsResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass