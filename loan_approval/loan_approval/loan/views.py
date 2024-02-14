from django.shortcuts import render, HttpResponse
import pickle as pk
import pandas as pd
import numpy as np
from xgboost import XGBClassifier as XG
import os

with open('model/pipe.pkl', 'rb') as f:
    pipe = pk.load(f)

# Create your views here.
def main(request):
    return render(request,'main.html')

def result(request):
    if request.method == 'POST':
        home = request.POST.get('home')
        intent = request.POST.get('intent')
        amount = request.POST.get('amount')
        income = request.POST.get('income')
        interest = request.POST.get('interest')
        default = request.POST.get('default')
        year = request.POST.get('year')
        age = request.POST.get('age')
        amount = int(amount)
        income = int(income)
        interest = float(interest)
        year = int(year)
        percent = float(round(amount/income,2))
        if default == 'Yes':
            default = 'Y'
        elif default == 'No':
            default = 'N'
        print(home,intent,year,income)

        input_df = pd.DataFrame({'Age':[age], 'Income':[income], 'Home':[home], \
                                 'Emp_length':[year], 'Intent':[intent], 'Amount':\
                                    [amount], 'Rate':[interest], 'Percent_income':\
                                        [percent], 'Default':[default]})
        prediction = pipe.predict(input_df)
        if prediction[0] == 0:
            context = {
                'result':'Rejected'
            }
            return render(request,'result.html',context)
        elif prediction[0] == 1:
            context = {
                'result':'Accepted'
            }
            return render(request,'result.html',context)
        return render(request,'result.html')
    return render(request,'main.html')