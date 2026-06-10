from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.


# def january(request):
#     return HttpResponse("Eat no meat for the entire month!")

# def february(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes every day!")

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Drink 1 gallon of water per day the entire month!",  
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",  
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",  
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        return HttpResponseRedirect(f"/challenges/{redirect_month}")
    except IndexError:
        return HttpResponseNotFound("Invalid month!")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges.get(month)
        if challenge_text:
            return HttpResponse(challenge_text)
        else:
            return HttpResponseNotFound("This month is not supported!")
    except KeyError:
        return HttpResponseNotFound("Invalid month!")
    
