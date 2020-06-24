class CommentRepliesResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '{"comment_id": 1, "commenter": {"user_id": 1, "name": "string", "profile_pic": "string"}, "commented_at": "string", "comment_content": "string"}',
            "response_serializer": "CommentSerializer",
            "response_serializer_import_str": "from fb_post.build.serializers.definitions.Comment.CommentSerializer import CommentSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass