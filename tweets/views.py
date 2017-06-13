from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Tweet
# Create your views here.
class TweetDetailView(DetailView):
    #template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

    def get_object(self):
        return Tweet.objects.get(id=1)


class TweetListView(ListView):
    queryset = Tweet.objects.all()
    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        #context["another_list"] = Tweet.objects.all()
        #print(context)
        return context
