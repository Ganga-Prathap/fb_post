from fb_post.models.reaction import Reaction

from .validations import (
    is_valid_user_id,
    is_valid_comment_id,
    is_valid_reaction_type
)

from .react_to_post import check_user_reaction


# Task-6
def react_to_comment(user_id, comment_id, reaction_type):

    is_valid_user_id(user_id)

    is_valid_comment_id(comment_id)

    is_valid_reaction_type(reaction_type)

    try:
        reaction_obj = Reaction.objects.get(
            reacted_by_id=user_id, comment_id=comment_id
        )

    except Reaction.DoesNotExist:
        Reaction.objects.create(
            reacted_by_id=user_id, comment_id=comment_id,
            reaction=reaction_type
        )

    else:
        check_user_reaction(reaction_obj, reaction_type)
