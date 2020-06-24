from django.db.models import Count, Q, F
from fb_post.models.post import Post
from fb_post.constants.reaction_enum import ReactionEnum


POSITIVE_REACTIONS = [
        ReactionEnum.THUMBSUP.value,
        ReactionEnum.LIT.value,
        ReactionEnum.LOVE.value,
        ReactionEnum.HAHA.value,
        ReactionEnum.WOW.value
    ]

NEGATIVE_REACTIONS = [
        ReactionEnum.SAD.value,
        ReactionEnum.ANGRY.value,
        ReactionEnum.THUMBSDOWN.value
    ]

# Task-10
def get_posts_with_more_positive_reactions():

    positive_count = Count('reactions', filter=Q(
        reactions__reaction__in=POSITIVE_REACTIONS))

    negative_count = Count('reactions', filter=Q(
        reactions__reaction__in=NEGATIVE_REACTIONS))

    post_objs_ids = list(Post.objects.annotate(p_count=positive_count)\
                        .annotate(n_count=negative_count)\
                        .filter(p_count__gt=F('n_count'))\
                        .values_list('id', flat=True))

    return post_objs_ids
