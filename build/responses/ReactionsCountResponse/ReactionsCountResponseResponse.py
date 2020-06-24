class ReactionsCountResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"count": 1}',
            "response_serializer": "ReactionsCountResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.ReactionsCountResponse.ReactionsCountResponse.ReactionsCountResponseSerializer import ReactionsCountResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass