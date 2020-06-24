from fb_post.models.reaction import Reaction
from .validations import is_valid_post_id
from .conversion_function_utils import get_user_details_dict


def get_user_reactions_on_post(reaction_obj):

    user_reaction_dict = get_user_details_dict(reaction_obj.reacted_by)
    user_reaction_dict['reaction'] = reaction_obj.reaction

    return user_reaction_dict

# Task-12
def get_reactions_to_post(post_id):

    is_valid_post_id(post_id)

    reaction_objs = Reaction.objects.filter(post_id=post_id)\
                            .select_related('reacted_by')

    users_reaction_list = []

    for reaction_obj in reaction_objs:
        users_reaction_list.append(get_user_reactions_on_post(reaction_obj))

    return users_reaction_list
