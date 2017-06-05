import json
import random
from datetime import datetime
from random import randrange

from dateutil.relativedelta import relativedelta
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def proxifier(request):
    accounts = Account.objects.all()

    return render(request, 'proxifier.html', {'accounts': accounts})


# AJAX endpoint for new client
def proxifier_ajax(request):
    if request.method == 'POST':
        response_data = {}
        dates = searcher_randomizer(3, 5)

        for d in dates:
            print d.strftime("%Y-%m-%d %H:%M")

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

    # selenizer = proxifier_aux.Selenium(1)
    # selenizer.google_search("Fernando Reinoso Barbero")


def date_range(start_date, end_date, period):
    rand_increment = randrange(1, 60)
    result = []
    nxt = start_date
    delta = relativedelta(**{period: rand_increment})
    while nxt <= end_date:
        result.append(nxt)
        nxt += delta
    return result


def searcher_randomizer(day_lenght, number_of_return_dates):
    start_date = datetime.now()
    reference_date = start_date.replace(hour=10, minute=0, second=0, microsecond=0)
    end_date = reference_date + relativedelta(days=day_lenght)
    final_date = end_date.replace(hour=23, minute=0, second=0, microsecond=0)

    date_array = date_range(start_date, final_date, 'minutes')
    return_array = []

    for _ in range(number_of_return_dates):
        choice = random.choice(date_array)
        date_array.remove(choice)
        return_array.append(choice)

    return return_array
