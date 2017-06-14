from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Tweet
# Create your views here.
class TweetDetailView(DetailView):
    #template_name = "tweets/detail_view.html"
    queryset = Tweet.objects.all()

#    def get_object(self):
#       return Tweet.objects.get(id=1)


class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        #context["another_list"] = Tweet.objects.all()
        #print(context)
        return context

def tweet_detail_view(request, pk=None): # pk == id
    #obj = Tweet.objects.get(pk=pk) # GET from database
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)