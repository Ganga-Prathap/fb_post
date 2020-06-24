class PostParameter(object):
    @staticmethod
    def get_param_name():
        param_names = {
            "parameter_name": "CreatePostParameter",
            "parameter_field_name": "post"
        }
        return param_names

    @staticmethod
    def get_serializer_class():
        serializer_options = {
            "param_serializer": "postSerializer",
            "param_serializer_import_str": "from fb_post.build.parameters.CreatePostParameter.post.postSerializer import postSerializer",
            "param_serializer_required": True,
            "param_serializer_array": False
        }
        return serializer_options
        

    @staticmethod
    def get_serializer_field():
        pass

    @staticmethod
    def get_url_regex():
        pass