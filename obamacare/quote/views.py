from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django import forms


from quote.models import Quote


class CreateQuote(CreateView):
    model = Quote
    template_name = "quote/create.html"
    fields = ['body', 'name']


class QuoteDetail(DetailView):
    model = Quote
    template_name = "quote/detail.html"


class QuoteUpvote(UpdateView):
    model = Quote
    fields = []

    def get_form_class(self, *args, **kwargs):

        class UpvoteForm(forms.ModelForm):
            upvote = forms.IntegerField()

            class Meta:
                model = Quote
                fields = []

            def __init__(self, *args, **kwargs):
                super(UpvoteForm, self).__init__(*args, **kwargs)

            def save(self):
                self.instance.upvote()

        return UpvoteForm

    def form_valid(self, form):
        # Make sure they haven't voted on this
        try:
            votes = self.request.session['upvotes']
        except:
            votes = []

        if not (form.instance.id in votes):
            form.save()
            votes.append(form.instance.id)
            self.request.session['upvotes'] = votes

        return HttpResponseRedirect(form.instance.get_absolute_url())


class QuoteDownvote(UpdateView):
    model = Quote

    def get_form_class(self, *args, **kwargs):

        class DownvoteForm(forms.ModelForm):
            downvote = forms.IntegerField()

            class Meta:
                model = Quote
                fields = []

            def __init__(self, *args, **kwargs):
                super(DownvoteForm, self).__init__(*args, **kwargs)

            def save(self):
                self.instance.downvote()

        return DownvoteForm

    def form_valid(self, form):
        try:
            votes = self.request.session['downvotes']
        except:
            votes = []
        if not (form.instance.id in votes):
            form.save()
            votes.append(form.instance.id)
            self.request.session['downvotes'] = votes
        return HttpResponseRedirect(form.instance.get_absolute_url())

@never_cache
def random_quote(request):
    random = Quote.objects.random()
    return HttpResponseRedirect(random.get_absolute_url())


class TopQuotes(ListView):
    model = Quote
    template_name = "quote/top.html"

    paginate_by = 36

    def get_queryset(self):
        qs = super(TopQuotes, self).get_queryset()
        return qs.order_by('-ranking')


class NewQuotes(ListView):
    model = Quote
    template_name = "quote/new.html"

    paginate_by = 36

    def get_queryset(self):
        qs = super(NewQuotes, self).get_queryset()
        return qs.order_by('-last_modified')
