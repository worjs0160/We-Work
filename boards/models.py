from django.db import models


class Board(models.Model):
    author = models.ForeignKey(
        "users.User",
        related_name="boards",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    board_num = models.CharField(max_length=8)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    view_cnts = models.IntegerField(min=0)
    contents = models.TextField(blank=True)
