from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

#dictionary with monthly challenges
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
#function with int month views
def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

#function with monthly_challenge (challenges/<month>) view
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
