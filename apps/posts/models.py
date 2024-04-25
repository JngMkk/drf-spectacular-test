from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    id = models.AutoField(_("id"), primary_key=True)
    title = models.CharField(_("제목"), max_length=30)
    name = models.CharField(_("이름"), max_length=20)
    content = models.TextField(_("본문"))
    created_at = models.DateTimeField(_("작성 날짜"), auto_now_add=True)
    updated_at = models.DateTimeField(_("수정 날짜"), auto_now=True)

    class Meta:
        db_table = "posts"
