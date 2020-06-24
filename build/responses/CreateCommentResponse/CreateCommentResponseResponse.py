class CreateCommentResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"comment_id": 1}',
            "response_serializer": "CreateCommentResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.CreateCommentResponse.CreateCommentResponse.CreateCommentResponseSerializer import CreateCommentResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass