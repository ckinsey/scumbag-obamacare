from django.conf.urls import patterns, url

from quote.views import CreateQuote, QuoteDetail, QuoteDownvote, QuoteUpvote, random_quote, TopQuotes, NewQuotes

urlpatterns = patterns('',
    url('^create/$', CreateQuote.as_view(), name="create-quote"),
    url('^view/(?P<pk>\d+)/$', QuoteDetail.as_view(), name="quote-detail"),
    url('^upvote/(?P<pk>\d+)/$', QuoteUpvote.as_view(), name="quote-upvote"),
    url('^downvote/(?P<pk>\d+)/$', QuoteDownvote.as_view(), name="quote-downvote"),
    url('^random/$', random_quote, name="random-quote"),
    url('^top/$', TopQuotes.as_view(), name="top-quotes"),
    url('^new/$', NewQuotes.as_view(), name="new-quotes"),
)
