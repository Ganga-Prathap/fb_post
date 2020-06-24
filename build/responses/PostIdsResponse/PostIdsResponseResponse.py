class PostIdsResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[1]',
            "response_serializer": "PostIdsResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.PostIdsResponse.PostIdsResponse.PostIdsResponseSerializer import PostIdsResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass