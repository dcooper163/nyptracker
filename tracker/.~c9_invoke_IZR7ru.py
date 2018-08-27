from django.shortcuts import render
import datetime

# Create your viewsfrom django.http 
from django.http import HttpResponse


def index(request):
    #return HttpResponse(' ' . {% for ticket in tickets %}<li>{{pet.name}}</li>{%endfor %} ' ')
      
    now = datetime.datetime.now()
    html = "<html><body>It bbbb is now %s.<p><ul></ul></p></body></html>" % now

    return HttpResponse(html)
    
    
def detail(request, ticket_number):
    return HttpResponse("You're looking at ticket %s." % ticket_number)

def results(request, ticket_number):
    response = "You're looking at the results of ticket %s."
    return HttpResponse(response % ticket_number)

def vote(request, ticket_number):
    return HttpResponse("You're voting on ticket %s." % ticket_number)