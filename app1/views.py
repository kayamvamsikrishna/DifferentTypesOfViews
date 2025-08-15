from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
from typing import Any
from app1.forms import *


# returning string as response by using FBV

def StringByFbv(request):
    return HttpResponse('<h1>StringByFbv</h1>')

# returning string as response by using CBV

class StringByCbv(View):#inherit from view class
    def get(self,request):
        return HttpResponse('<h1>StringByCbv</h1>')

# returning html page as response by using FBV

def HtmlByFbv(request):
    return render(request,'HtmlByFbv.html')

# returning html page as response by using CBV

class HtmlByCbv(View):
    def get(self,request):
        return render(request,'HtmlByCbv.html')


 # Inserting data into school by using FBV

def insertbyfbv(request):
    d={'ESFO':SchoolForm()}#form object in the form of dictionary
    if request.method=='POST':#initially it is false, after submitting the data it will be activated, activate in the sense the condition get true, then control will entered into this block
        SFDO=SchoolForm(request.POST) #submitted data
        if SFDO.is_valid():
            SFDO.save() #save in the sense the data will be stored in the database 
            return HttpResponse('insert_by_fbv is done')
        else:
            return HttpResponse('insert_by_fbv is failed')
    
    return render(request,'insertbyfbv.html',d)

#Class-Based Views (CBV)
# Inserting data into school by using CBV

class InsertByCbv(View):
    def get(self,request):#GET------In this class first this method will be executed and html page is rendered.example: InsertByCbv.html
        d={'ESFO':SchoolForm()}#take the form in the form of dictionary and send this dict to html page and then render the html page
        return render(request,'InsertByCbv.html',d)
    #After that a beautifual page will be displayed in the chrome browser,....
    #Now you add the data or type the data and then tap on the submit button.
    def post(self,request):#POST----After submitted the data this method will activated 
        SFDO=SchoolForm(request.POST)#SUBMITTED DATA
        if SFDO.is_valid():#PERFORM VALIDATIONS
            SFDO.save()#SAVE THE SUBMITTED DATA IN THE DATABASE 
            return HttpResponse('insert_by_cbv is done') #THEN RETURN THE RESPONSE
        else:
            return HttpResponse('insert_by_cbv is failed')
    
#Generic Class-Based Views
#TEMPLATE VIEW
class HtmlbyTV(TemplateView):
    template_name='HtmlbyTV.html'

class SendDataByTV(TemplateView):
    template_name='SendDataByTV.html'
    ''' **kwargs: This allows the method to accept any number of keyword arguments. Django often passes values here automatically 
         Any: This is a type hint from Python's typing module, indicating that the values in kwargs can be of any type.
         -> dict[str, Any]
        This is a type hint that says this method will return a dictionary where:
            Keys are strings (e.g., 'name', 'age')
            Values can be of any type (e.g., strings, integers, form objects)'''
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: 
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='KVK'
        ECDO['age']=22
        ECDO['ESFO']=StudentForm()
        return ECDO
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():#validations
            SFDO.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('Invalid')
        
