import factory
from fb_post.models.user import User
from fb_post.models.post import Post
from datetime import datetime


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: 'name%d' % n)
    profile_pic = factory.Sequence(lambda n: 'https://profile%d' % n)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    content = factory.Sequence(lambda n: 'post_content%d' % n)
    posted_at = factory.LazyFunction(datetime.now)
    posted_by = factory.SubFactory(UserFactory)
