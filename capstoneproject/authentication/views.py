from django.shortcuts import render, redirect
from authentication.models import User
from django.contrib import messages
from django.db import connection
from django.contrib.auth.models import auth
from django.template.response import TemplateResponse
# Create your views here.

def register(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('password'):
            saverecord = User()
            saverecord.username = request.POST.get('username')
            saverecord.first_name = request.POST.get('first_name')
            saverecord.last_name = request.POST.get('last_name')
            saverecord.password = request.POST.get('password')
            saverecord.save()
            messages.success(request, "New Account Created!")
            return render(request, "register.html")
    else:
        return render(request, "register.html")

def login(response):
    if response.method == 'POST':   
        if response.POST.get('username') and response.POST.get('password'):            
            query = f"""SELECT username , password from user where username = "{response.POST.get('username')}" and password ="{response.POST.get('password')}" """
            cursor = connection.cursor()
            cursor.execute(query)
            query_data = cursor.fetchall()
            print(query_data)

            if len(query_data) != 0:                   
                messages.success(response, "Logged In Succesfully")
                # args = {}
                # data = query_data[0][0]
                # args['first'] = data
                return redirect("/index", username=query_data[0][0])
                #return TemplateResponse(response, "index.html", args)
            else:    
                messages.error(response, "Invalid Credentials")
                return render(response, "login.html")
    else:
        return render(response,"login.html")
