from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review

# Create your views here.


def review(request):
    # form = None   # apparently python variables dont have block scoping, so form can be accessed outside of if-block
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            review = Review(
                user_name=data["user_name"],
                review_text=data["review_text"],
                rating=data["rating"]
            )
            review.save()
            return HttpResponseRedirect('/thank_you')

    # if request.method is not "POST" create a blank form
    else:
        form = ReviewForm()

    return render(request, 'reviews/review.html', {
        "form": form
    })


def thank_you(request):
    return render(request, 'reviews/thank_you.html')