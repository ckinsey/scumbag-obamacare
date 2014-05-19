from django.views.generic import TemplateView
from quote.models import Quote

class Homepage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):

        context = {
            'top_quotes': Quote.objects.all().order_by('-ranking')[:36],
        }

        return context