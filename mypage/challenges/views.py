from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    "december": "Learn spanish everyday"
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
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    return HttpResponse(response_data)


def index(request):
    response_data = "<ol>"
    months = list(monthly_challenges.keys())
    for i in range(len(months)):
        link = reverse("month-challenge", args=[months[i]])
        response_data = response_data + \
            f"<h2><li><a href={link}>{months[i]}</a></li></h2>"
    response_data = response_data + "</ol>"
    return HttpResponse(response_data)
