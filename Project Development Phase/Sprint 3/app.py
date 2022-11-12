#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 17:32:15 2022

@author: tirumal
"""

from flask import Flask,render_template,request,render_template_string
import warnings
warnings.filterwarnings('ignore')

app=Flask(__name__)


#import model
import pickle
model = pickle.load(open('95%.pkl','rb'))

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/home')
def homePage():
    return render_template("home.html")

'''@app.route('/team')
def team():
    return render_template('team.html')'''

@app.route('/prediction')
def predict_test():
    return render_template('predict.html')

@app.route('/predict',methods=['post'])
def predict():
  
    age= request.form["age"]
    bp= request.form["bp"]
    sg= request.form["sg"]
    al= request.form["al"]
    su= request.form["su"]
    rbc= request.form["rbc"]
    pc= request.form["pc"]
    pcc= request.form["pcc"]
    ba= request.form["ba"]
    bgr= request.form["bgr"]
    bu= request.form["bu"]
    sc= request.form["sc"]
    sod= request.form["sod"]
    pot= request.form["pot"]
    hemo= request.form["hemo"]
    pcv= request.form["pcv"]
    wbcc= request.form["wbcc"]
    rbcc= request.form["rbcc"]
    htn= request.form["htn"]
    dm= request.form["dm"]
    cad= request.form["cad"]
    appet= request.form["appet"]
    pe= request.form["pe"]
    ane= request.form["ane"]
    values = [[int(age), int(bp), float(sg), int(al), int(su), int(rbc), int(pc), int(pcc), int(ba), int(bgr), int(bu), float(sc), int(sod), float(pot), float(hemo), int(pcv), int(wbcc), float(rbcc), int(htn), int(dm), int(cad), int(appet), int(pe), int(ane)]]
    #values=[[57, 92, 2.0, 1, 3, 1, 1, 0, 0, 129, 36, 2.0, 150, 4, 12.0, 33, 4500, 5.0, 1, 0, 1, 1, 0, 0]]
    print(values)
    output=model.predict(values)
    print(output)
    #output[0]==1
    if(output[0]==0): return render_template("failure.html")#output="CKD"
    else: return render_template("success.html")#output="No CKD" 
    #return render_template("index.html",output = "the predicted result is  " + output)    
    
if __name__ == '__main__':
    app.static_folder='static'
    app.run(debug=True)