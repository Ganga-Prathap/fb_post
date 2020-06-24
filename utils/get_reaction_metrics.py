from django.db.models import Count
from fb_post.models.reaction import Reaction
from .validations import is_valid_post_id


# Task-8
def get_reaction_metrics(post_id):

    is_valid_post_id(post_id)

    post_reactions = Reaction.objects.values('reaction')\
        .filter(post_id=post_id)\
        .annotate(count=Count('reaction'))

    reaction_matrices_dict = {}
    for post_reaction in  post_reactions:
        reaction = post_reaction['reaction']
        count = post_reaction['count']
        reaction_matrices_dict[reaction] = count

    return reaction_matrices_dict
