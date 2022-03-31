from django.shortcuts import render
import csv
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "dashboard/index.html")

def predictions(request):
    return render(request, "dashboard/predictions.html")

def diabetes(request):
    return render(request, "dashboard/diabetes.html")

def dataset(request):
     return render(request, "dashboard/dataset.html")
    


def about(requst):
    return render(requst, "dashboard/about.html")


def getPredictions(glucoe_,bmi_,age_):

    import pickle 
    model= pickle.load(open('diabets.model_svm','rb'))
    prediction=model.predict([[glucoe_,bmi_,age_]])
    if prediction[0]==0:
        return "Diyabet Hastası Değil" 
    else:
        return "Diyabet Hastası"

  
def result(request):
    glucose = int(request.GET['glucose'])
    bmi = int(request.GET['bmi'])
    age = int(request.GET['age'])
    result = getPredictions(glucose, bmi, age)
    return render(request, "dashboard/result.html", {'result':result})







 