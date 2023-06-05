from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# dictionary with monthly challenges
monthly_challenges = {
    "january": "Eat no sweets for the entire month",
    "february": "Work out for at least 20 minutes every day!",
    "march": "Read book for 30 minutes every day!",
    "april": "Walk for 20 minutes every day",
    "may": "Cook for yourself four times a week",
    "june": "Eat no meat for the entire month",
    "july": "Dont drink any alcohol",
    "august": "Paint one piece every week",
    "september": "Dont use your phone more than hour per day",
    "october": "Work out at least 30 minutes every day!",
    "november": "Don't watch netflix entire month",
    "december": None
}


# Create your views here.
# function with int month views
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_url = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_url)

# function with monthly_challenge (challenges/<month>) view


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        raise Http404()


# function with months list (/challenges)
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })
    
