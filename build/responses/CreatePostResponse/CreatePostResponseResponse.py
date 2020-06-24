class CreatePostResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"post_id": 1}',
            "response_serializer": "CreatePostResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.CreatePostResponse.CreatePostResponse.CreatePostResponseSerializer import CreatePostResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass