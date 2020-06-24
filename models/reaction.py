from django.db import models
from .user import User
from .post import Post
from .comment import Comment
from fb_post.constants.reaction_enum import ReactionEnum

class Reaction(models.Model):

    CHOICES = [
        (react.value, react.name)
        for react in ReactionEnum
    ]

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='reactions'
    )

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        related_name = 'reactions'
    )

    reaction = models.CharField(
        choices=CHOICES,
        max_length=100
    )

    reacted_at = models.DateTimeField(
        auto_now=True
    )

    reacted_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.reaction
