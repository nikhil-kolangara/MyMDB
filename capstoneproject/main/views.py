from django.shortcuts import render

# Create your views here.

def index(response):
    # username = response.GET.get('username')
    # print(username)
    # context = {'username':username}
    return render(response, "index.html")