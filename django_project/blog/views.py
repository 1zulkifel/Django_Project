from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

post= [
    {'Author':'Zulkifel',
     'title':'Post 1',
     'content':'First Post Content',
     'Date_posted':'Feb 18 2024'},
         {'Author':'Ramzan',
     'title':'Post 2',
     'content':'Second Post Content',
     'Date_posted':'Feb 15 2024'},
         {'Author':'Najeeb',
     'title':'Post 3',
     'content':'Third Post Content',
     'Date_posted':'Feb 17 2024'}]

def home(request):
    context={'post':post}
    return render (request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html', {'title':'about'})