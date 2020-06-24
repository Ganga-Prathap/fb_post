import factory
from fb_post_v2.models import user

"""
class User:

    def __init__(self, fname: str, lname: str):
        self.fname = fname
        self.lname = lname
"""

class UserFactory(factory.Factory):

    class Meta:
        model = user.User
    
    name = 'Ganga'
