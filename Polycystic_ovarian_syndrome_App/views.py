from django.shortcuts import render
from Polycystic_ovarian_syndrome_App.models import User, History
from Polycystic_ovarian_syndrome_App import train_symtoms
from Polycystic_ovarian_syndrome_App import predict
from django.db.models import Q
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import shutil
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier


from sklearn import svm


# Create your views here.
def index(request):
    return render(request,'index.html')
def graphs(request):
    return render(request,'user/graphs.html')

def user(request):
    return render(request,'user/index.html')

def registration(request):
    return render(request,'user/registration.html')

def saveUser(request):
    if request.method == 'POST':
        farmername = request.POST['uname']
        contactNo = request.POST['contactNo']
        emailId = request.POST['emailId']
        address = request.POST['address']
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(
            Q(email=emailId) | Q(contact=contactNo) | Q(user_name=username)
        ).first()

        has_error = False
        error = ''

        if user != None and user.user_name == username:
            has_error = True
            error = 'Duplicate user name'

        if user != None and user.email == emailId:
            has_error = True
            error = 'Duplicate email'

        if user != None and user.contact == contactNo:
            has_error = True
            error = 'Duplicate contact number'

        if has_error:
            return render(request, "user/registration.html", {'error': error})

        user = User(name=farmername, contact=contactNo, email=emailId,
                    address=address, user_name=username, password=password)
        user.save()

        return render(request, "user/registration.html", {'success': 'User Added Successfully'})
    else:
        return render(request, 'user/registration.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.values_list('password', 'id', 'name').\
            filter(user_name=request.POST['username'])

        user = User.objects.filter(
            user_name=username, password=password).first()

        if user == None:
            return render(request, 'user/index.html', {'error': 'Invalid login credentials'})

        request.session['userid'] = user.id
        request.session['userName'] = user.name

        return render(request, 'user/userHome.html')

    else:
        return render(request, 'user/index.html')
    
def uploadImage(request):
    return render(request,'user/upload.html')

def homepage(request):
    return render(request,'user/userHome.html')

def home(request):

    if request.method == "GET":
        return render(request, 'home.html')

    if request.method == "POST":
        image = request.FILES['test1']
        id = request.POST['id']

        shutil.rmtree(os.getcwd() + '\\media\\upload')

        path = default_storage.save(
            os.getcwd() + '\\media\\upload\\input.png', ContentFile(image.read()))
        
        path1 = "/media/upload/input.png"
        result = predict.process()
        history = History.objects.filter(id = id).get()
        history.result2 = result
        history.save()
        resu=""
        if result == "Normal Ovary":
            resu = "Nothing to worry..."
        elif result=="PCOS":
            resu = "Do some Diet!!"
        else:
            resu = "Not an ultrasound image"
            
        
    return render(request, "user/result.html", {'result': result, "resu" : resu, 'path':path1})

def testagain(request):
    return render(request, "user/uploadDetails.html")

def history(request):
    user_id = request.session['userid']
    histories = History.objects.filter(user_id = user_id).order_by('-id')
    return render(request, "user/history.html", {'histories' : histories})


def uploadDetails(request):
    if request.method == "POST":
        height = request.POST['height']
        weight = request.POST['weight']
        bmi = request.POST['bmi']
        hirsutism = request.POST['hirsutism']
        skin = request.POST['skin']
        acene = request.POST['acene']
        menstrual = request.POST['menstrual']
        sleep = request.POST['sleep']
        hair = request.POST['hair']
        user_id = request.session['userid']

        height_value = 0
        weight_value = 0
        bmi_value = 0
        if float(height) > 180 and float(weight) > 50 and float(bmi) > 25 :
            height_value = 1
            weight_value = 1
            bmi_value = 1

        dataset=pd.read_csv('media/features.csv')
        dataset.shape
        X=np.array(dataset.iloc[:,:-1])
        X=X.astype(dtype='int')
        Y=np.array(dataset.iloc[:,-1])
        Y=Y.reshape(-1,)

        X_train, X_test, y_train, y_test =train_test_split(X,Y,test_size=0.25,
                                                        random_state=42)
        print(X_train.shape)

        model_RR=RandomForestClassifier(n_estimators=100,random_state=42)
        model_RR.fit(X_train,y_train)
        
        X_test = [height_value, weight_value, bmi_value, hirsutism, skin, acene, menstrual, sleep, hair]
        print(X_test)

        y_predicted_RR=model_RR.predict(np.asarray(X_test).reshape(1,-1))
        print(y_predicted_RR)
        # confusion=confusion_matrix(y_test,y_predicted_RR)
        # accuracy_score(y_test,y_predicted_RR)
        # accuracy_score(y_test,y_predicted_RR)

        result = str(y_predicted_RR[0])
        history = History(user_id = user_id, height = height, weight = weight, bmi = bmi, hirsutism = hirsutism, skin = skin, acene = acene, menstrual = menstrual, sleep = sleep, hair = hair, result1 = result)
        history.save()
        history_id = history.id
        res = "0"
        if result == "1":
            res ="1"
            result= "You may have polycystic ovarian syndrom"
            return render(request, "user/upload.html", {'result' : result, 'res' : res, 'history_id' : history_id})
        else:
            result= "You dont have polycystic ovarian syndrom"
            resu = "You are healthier!!!!"
            return render(request, "user/result.html", {'result' : result, 'resu' : resu, 'res' : res})
    else:
        return render(request, "user/uploadDetails.html")

