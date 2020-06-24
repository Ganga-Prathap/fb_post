from django.db.models import Count
from fb_post.models.reaction import Reaction


# Task-7
def get_total_reaction_count():
    reactions_count = Reaction.objects.aggregate(count=Count('id'))

    return reactions_count
