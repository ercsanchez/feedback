from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import ReviewForm

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, 'reviews/review.html', {
            'form': form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank_you')

        return render(request, 'reviews/review.html', {
            'form': form
        })


# function based view no longer used
def review(request):
    # form = None   # apparently python variables dont have block scoping, so form can be accessed outside of if-block
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank_you')

    # if request.method is not "POST" create a blank form
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {
        "form": form
    })


def thank_you(request):
    return render(request, 'reviews/thank_you.html')
