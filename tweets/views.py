from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView

from .models import Tweet
from .forms import TweetModelForm


class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = "/tweet/create/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context = {
        "form":form
    }
    return render(request, 'tweets/create_view.html', context)

