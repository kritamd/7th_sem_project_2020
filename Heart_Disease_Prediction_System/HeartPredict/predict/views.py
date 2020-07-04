import csv,io
from django.shortcuts import render
from .forms import Predict_Form
from .data_provider import *
from accounts.models import UserProfileInfo
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from sklearn.preprocessing import StandardScaler


def PredictRisk(request,pk):
    predicted=False
    predictions={}
    if request.session.has_key('user_id'):
        u_id=request.session['user_id']

    if request.method == 'POST':
        form=Predict_Form(data=request.POST)
        profile=get_object_or_404(UserProfileInfo,pk=pk)

        if form.is_valid():
            features = [[form.cleaned_data['age'], form.cleaned_data['sex'], form.cleaned_data['cp'],
                         form.cleaned_data['resting_bp'], form.cleaned_data['serum_cholesterol'],
                         form.cleaned_data['fasting_blood_sugar'], form.cleaned_data['resting_ecg'],
                         form.cleaned_data['max_heart_rate'], form.cleaned_data['exercise_induced_angina'],
                         form.cleaned_data['st_depression'], form.cleaned_data['st_slope'],
                         form.cleaned_data['number_of_vessels'], form.cleaned_data['thallium_scan_results']]]

            standard_scalar=GetStandardScalerForHeart()
            features=standard_scalar.transform(features)
            LogisticRegressionClassifier=GetClassifierForHeart()

            predictions={
                'LogisticRegression':str(LogisticRegressionClassifier.predict(features)[0])
            }

            pred=form.save(commit=False)


            result=False
            if predictions['LogisticRegression'] == 1:
                result=True
                pred.target=1

            else:
                pred.target=0

            pred.profile=profile

            pred.save()
            predicted=True

            colors={}


            if predictions['LogisticRegression']=='0':
                colors['LR']="table-success"

            else:
                colors['LR']="table-danger"

    if predicted:
        return render(request,'predict.html',
                      {'form':form,'predicted':predicted,'user_id':u_id,
                       'predictions':predictions,'result':result,'colors':colors})

    else:
        form=Predict_Form()

        return render(request,'predict.html',
                      {'form':form,'predicted':predicted,'user_id':u_id,'predictions':predictions})