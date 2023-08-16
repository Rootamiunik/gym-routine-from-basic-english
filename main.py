import requests
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

#---------------------------------Constant----------------------------#
SHEETY_ENDPOINT_POST = os.getenv("SHEETY_API_KEY")
SHEETY_API_KEY = os.getenv("SHEETY_API_KEY")

EXERCISE_ENDPOINT = os.getenv('EXERCISE_ENDPOINT')
NUTRITIONIX_API_ID =  os.getenv('NUTRITIONIX_API_ID')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')

#----------------------------Paremeter--------------------------------#
NUTRITIONIX_API_PARMS = {

 "query": input('Tell me what exercise you did: '),
 "gender":"male",
 "weight_kg":58,
 "height_cm":162,
 "age":17
}

#-----------------------Headers-------------------------------#
NUTRITIONIX_API_HEADERS = {
    'x-app-id':NUTRITIONIX_API_ID,
    'x-app-key':NUTRITIONIX_API_KEY,
}
SHEETY_API_HEADER = {
    'Authorization': f'Bearer {SHEETY_API_KEY}',

}

#------------------------server request--------------------#
server_request_exercise = requests.post(url=EXERCISE_ENDPOINT,json=NUTRITIONIX_API_PARMS,headers=NUTRITIONIX_API_HEADERS)
data = server_request_exercise.json()

#------------------------Date/time management----------------#
date = dt.datetime.now().strftime("%Y/%m/%d")
time = dt.datetime.now().strftime("%H:%M:%S")


#--------------------main-------------------------#
for num in range(len(data['exercises'])):
    sheet_inputs = {
        'workout': {
            "date": date,
            "time": time,
            "exercise":data['exercises'][num]['user_input'].title(),
            "timespent":str(data['exercises'][num]['duration_min']),
            "calories":data['exercises'][num]['nf_calories'],
        }
    }
    print(type(sheet_inputs['workout']['timespent']))
    server_request_shitty = requests.post(url=SHEETY_ENDPOINT_POST,json=sheet_inputs,headers=SHEETY_API_HEADER)



