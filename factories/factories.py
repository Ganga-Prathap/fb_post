import factory
import factory.fuzzy
from datetime import datetime
from freezegun import freeze_time
from fb_post.models import User, Post, Comment, Reaction


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


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    content = factory.Sequence(lambda n: 'comment_content%d' %n)
    commented_at = factory.LazyFunction(datetime.now)
    commented_by = factory.SubFactory(UserFactory)


class ReplyCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    parent_comment = factory.SubFactory(CommentFactory,
        post=factory.LazyAttribute(lambda obj: obj.factory_parent.post))
    content = factory.Sequence(lambda n: 'reply_comment_content%d' %n)
    commented_at = factory.LazyFunction(datetime.now)
    commented_by = factory.SubFactory(UserFactory)


class ReactionToPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    post = factory.SubFactory(PostFactory)
    reaction = factory.fuzzy.FuzzyChoice(Reaction.CHOICES, getter=lambda c: c[0])
    reacted_at = factory.LazyFunction(datetime.now)
    reacted_by = factory.SubFactory(UserFactory)


@freeze_time('2020-06-23')
class ReactionToCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    comment = factory.SubFactory(CommentFactory)
    reaction = factory.fuzzy.FuzzyChoice(Reaction.CHOICES, getter=lambda c: c[0])
    reacted_at = factory.LazyFunction(datetime.now)
    reacted_by = factory.SubFactory(UserFactory)
