from django.shortcuts import render
# from .models import *
# from django.contrib.sites.shortcuts import current_site
from django.contrib.auth.models import User
from django.db import connections
import mysql.connector
import datetime
from django import db
import json
from django.http import JsonResponse
# Create your views here.
from scopes import settings
from django.views.decorators.csrf import csrf_exempt
def database_create(usr):
    database_id = usr.username #just something unique
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Password@123"
    )
    mycursor = mydb.cursor()
    print (mycursor)
    s = "CREATE DATABASE"+' ' +database_id
    print (s)
    mycursor.execute(s)
    return True
    #     print (database_id)
    #     newDatabase = {}
    #     newDatabase["id"] = database_id
    #     newDatabase['ENGINE'] = 'django.db.backends.mysql'
    #     newDatabase['NAME'] = database_id
    #     newDatabase['USER'] = 'root'
    #     newDatabase['PASSWORD'] = 'Password@123'
    # connections.databases[database_id] = newDatabase
    # save_db_settings_to_file(newDatabase)
# def data(request):
#     p = Post.objects.filter(site=current_site)
@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    user_name = data['user_name']
    if User.objects.filter(username=data['user_name']).exists():
        return JsonResponse({'response':"User already exist",'status':"Fail"})
    else:
        usr,created = User.objects.get_or_create(username=user_name)
        usr.save()
        database_create(usr)
        return JsonResponse({'response':"User created sucessfully",'status':"Sucess"})
        # database_id = usr.username #just something unique
        # mydb = mysql.connector.connect(
        #   host="localhost",
        #   user="root",
        #   passwd="Password@123"
        # )
        # mycursor = mydb.cursor()
        # print (mycursor)
        # s = "CREATE DATABASE"+' ' +database_id
        # print (s)
        # mycursor.execute(s)

#db = User.objects.get(username=user_name)

def save_db_settings_to_file(db_settings):
    #path_to_store_settings = "/home/karthick/Music/scopes/database_settings/"
    newDbString = """
    DATABASES['%(id)s'] = {
        'ENGINE': '%(ENGINE)s', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%(NAME)s',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'Password@123',                  # Not used with sqlite                     # Set to empty string for default. Not used with sqlite3.
    }
    """ % db_settings
    file_to_store_settings = os.path.join(db_settings['id'] + ".py")
    print (file_to_store_settings)
    f = open(file_to_store_settings, "a")
    f.write(newDbString)

# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
from django.http import HttpResponse
def data(self):
    s = self.META['HTTP_HOST']
    return HttpResponse("{}".format(self.META['HTTP_HOST']))
