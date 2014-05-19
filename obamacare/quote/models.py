from random import randint

from django.db import models
from django.db.models import Count

from django.core.urlresolvers import reverse

class QuoteManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        print random_index
        return self.all()[random_index]

class Quote(models.Model):

    user = models.ForeignKey('auth.User', null=True)
    name = models.CharField("Your name", max_length=128, default="anonymous")
    body = models.TextField("Obamacare...")

    positive = models.PositiveIntegerField(default=1)
    negative = models.PositiveIntegerField(default=0)

    ranking = models.IntegerField(default=1)

    last_modified = models.DateTimeField(auto_now_add=True)

    objects = QuoteManager()

    def get_absolute_url(self):
        return reverse("quote-detail", args=[self.id])

    def save(self, *args, **kwargs):
        self.ranking = self.positive - self.negative
        super(Quote, self).save()

    def upvote(self):
        self.positive += 1
        self.save()

    def downvote(self):
        self.negative += 1
        self.save()