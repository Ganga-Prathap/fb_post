class UserPostDetailResponseResponse(object):

    @staticmethod
    def get_response():
        response = {
            "response_data": '[{"post_id": 1, "posted_by": {"user_id": 1, "name": "string", "profile_pic": "string"}, "posted_at": "string", "post_content": "string", "reactions": {"count": 1, "type": ["string"]}, "comments": [{"comment_id": 1, "commenter": {"user_id": 1, "name": "string", "profile_pic": "string"}, "commented_at": "string", "comment_content": "string", "reactions": {"count": 1, "type": ["string"]}, "replies_count": 1, "replies": [{"comment_id": 1, "commenter": {"user_id": 1, "name": "string", "profile_pic": "string"}, "commented_at": "string", "comment_content": "string", "reactions": {"count": 1, "type": ["string"]}}]}], "comments_count": 1}]',
            "response_serializer": "UserPostDetailResponseSerializer",
            "response_serializer_import_str": "from fb_post.build.responses.UserPostDetailResponse.UserPostDetailResponse.UserPostDetailResponseSerializer import UserPostDetailResponseSerializer",
            "response_serializer_array": False,
        }
        return response


    @staticmethod
    def get_response_headers_serializer():
        pass