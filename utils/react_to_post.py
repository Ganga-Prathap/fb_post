from datetime import datetime
from fb_post.models.reaction import Reaction

from .validations import (
    is_valid_user_id,
    is_valid_post_id,
    is_valid_reaction_type
)


def delete_reaction_object(reaction_obj):

    reaction_obj.delete()


def update_reaction_object(reaction_obj, reaction_type):

    reaction_obj.reaction = reaction_type
    reaction_obj.reacted_at = datetime.now()
    reaction_obj.save()


def check_user_reaction(reaction_obj, reaction_type):

    is_reaction_same = reaction_obj.reaction == reaction_type

    if is_reaction_same:
        delete_reaction_object(reaction_obj)
    else:
        update_reaction_object(reaction_obj, reaction_type)


# Task-5
def react_to_post(user_id, post_id, reaction_type):

    is_valid_user_id(user_id)

    is_valid_post_id(post_id)

    is_valid_reaction_type(reaction_type)

    try:
        reaction_obj = Reaction.objects.get(
            post_id=post_id, reacted_by_id=user_id
        )

    except Reaction.DoesNotExist:
        Reaction.objects.create(
            reacted_by_id=user_id, post_id=post_id,
            reaction=reaction_type
        )

    else:
        check_user_reaction(reaction_obj, reaction_type)
