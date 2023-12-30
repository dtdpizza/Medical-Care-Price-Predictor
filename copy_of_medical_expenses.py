# -*- coding: utf-8 -*-
"""Copy of Medical_expenses.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DBZNodBZvQNQ9KTEOdUl9w0NbeKVHZoM
"""

import requests
import json
import math


def get_prediction(data={"age":41,"sex":"male","children":0,"smoker":"no","bmi":34.545,"region":"southeast"}):
  url = 'https://askai.aiclub.world/8439238b-56fd-4afe-9664-0ac4079c1e7e'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  #print(response)
  return response
print("Please Answer the following questions.")
print("For question 1 please do not put 0, negative numbers, or fractions or random words.")
print("For question 2 only male and female.")
print("For question 3 enter how many kids you have as an integer.")
print("For question 4 the choices are yes and no WITH the lowercase letters.")
print("For question 5 enter a decimal or whole number.")
print("For question 6 choices are northeast, northwest, southwest, southeast(DIRECT SPELLING).")
#age = input("Age: ")
flag=1
while flag==1:
  age = input("Age: ")
  try:
    age = int(age)
    if age > 0:
      flag=0
  except ValueError:
    print("Please reread the instructions before entering again.")

age = float(age)
age = math.floor(age)

if int(age) <= 0:
  print("Please reread the instructions before entering again.")
  age = input("Age: ")
else:
  print("Your age was rounded to", age)

gender = input("Gender: ")
while gender != "male" and gender != "female":
  print("Please reread the instructions before entering again.")
  gender = input("Gender: ")

flag=1
while flag==1:
  children = input("Children: ")
  try:
    children = int(children)
    if children > 0:
      flag=0
  except ValueError:
    print("Please reread the instructions before entering again.")

smoker = input("Smoker: ")
while smoker != "yes" and smoker != "no":
  print("Please reread the instructions before entering again.")
  smoker = input("Smoker: ")
flag=1
while flag==1:
  bmi = input("BMI: ")
  try:
    bmi = float(bmi)
    bmi = math.floor(bmi)
    if bmi > 0:
      flag=0
  except ValueError:
    print("Please reread the instructions before entering again.")

region = input("Region: ")
while region != "southwest" and region != "northwest" and region != "southeast" and region != "northeast":
  print("Please reread the instructions before entering again.")
  smoker = input("Region: ")
prediction = get_prediction(data={"age":int(age),"sex":gender,"children":int(children),"smoker":smoker,"bmi":float(bmi),"region":region})
predicted_label = json.loads(json.loads(prediction)["body"])["predicted_label"]
print("Price: ", predicted_label)