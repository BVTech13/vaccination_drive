from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django.utils.crypto import get_random_string
from datetime import datetime,timedelta
from datetime import date

from vaccination.models import registration,user,placeOne,placeTwo,placethree,placeFour
from vaccination.serializers import registrationSerializer,userSerializer,placeOneSerializer,placeTwoSerializer,placethreeSerializer,placeFourSerializer

@api_view(['GET'])
def ShowAll(request):
    register = registration.objects.all()
    registration_serializer=registrationSerializer(register,many=True)
    return JsonResponse({'status': 200,'response':registration_serializer.data},safe=False)


@api_view(['POST'])
def CreateUser(request):
    register=JSONParser().parse(request)
    user_dob = register["user_dob"]
    date_object = datetime.strptime(user_dob, '%Y-%m-%d').date()
    age = calculateAge(date_object)
    if age > 45:
        registration_serializer=registrationSerializer(data=register)
        if registration_serializer.is_valid():
            registration_serializer.save()
            id = get_random_string(12)
            user.objects.create(register_number = id, user_id=register["aadhar_number"])
            return JsonResponse({'status':200,'response':"Registarion has been completed successfully and your beneficiary ID is "+ id},safe=False)
        return JsonResponse({'status':400,'response':"Failed to Add"},safe=False)
    else:
        return JsonResponse({'status':200,'response':"Your not allowed to register for vaccination since you are below 45!"},safe=False)

@api_view(['GET'])
def viewUserDeatils(request, pk):
    try:
        user_data = user.objects.get(register_number=pk)
        user_serializer = userSerializer(user_data, many=False)
        return JsonResponse({'status':200,'response':user_serializer.data},safe=False)
    except Exception as e:
        return JsonResponse({'status':200,'response':"Id not found"}, safe=False)

@api_view(['POST'])
def vaccineRegistration(request):
    register=JSONParser().parse(request)
    user_data = user.objects.get(register_number=register['BID'])
    user_serializer = userSerializer(user_data, many=False)
    dose=findDose(user_serializer.data)
    if dose==None:
        return JsonResponse({'status':200,'response':"please cancel existing registration for vaccination"}, safe=False)
    slot=findSlot(register)
    if slot==None:
        return JsonResponse({'status':200,'response':"please enter avaliable slots for vaccination"}, safe=False)
    v_date,summary=validateDate(register["date"],dose,user_serializer.data["first_dose_date"])
    if v_date == True:
        place=FindPlace(slot,register["date"],dose)
        if place != None:
            post_data=postUserData(dose,slot,place,register["date"])
            post_data["register_number"]=user_serializer.data["register_number"]
            post_data["user"]=user_serializer.data["user"]
            user_serializer = userSerializer(user_data,data=post_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse({'status':200,'response':"Successfully booked appointment on "+register["date"]+" "+slot+" at "+place},safe=False)
        else:
            return JsonResponse({'status':200,'response':"All vaccination center has been full"},safe=False)
    else:
        return JsonResponse({'status':200,'response':summary}, safe=False)
@api_view(['POST'])
def upadteStatus(request):
    register=JSONParser().parse(request)
    user_data = user.objects.get(register_number=register['BID'])
    user_serializer = userSerializer(user_data, many=False)
    dose=findDoseStatus(user_serializer.data)
    if dose == None:
        return JsonResponse({'status':200,'response':"Nothing to update!"}, safe=False)
    else:
        post_data={dose:True}
        post_data["register_number"]=user_serializer.data["register_number"]
        post_data["user"]=user_serializer.data["user"]
        user_serializer= userSerializer(user_data,data=post_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse({'status':200,'response':"Successfully upadated!"}, safe=False)
        return JsonResponse({'status':400,'response':"Failed to update!"}, safe=False)

@api_view(['POST'])
def cancelAppointment(request):
    register=JSONParser().parse(request)
    user_data = user.objects.get(register_number=register['BID'])
    user_serializer = userSerializer(user_data, many=False)
    dose=findDoseStatus(user_serializer.data)
    if dose == None:
        return JsonResponse({'status':200,'response':"Nothing to cancel"}, safe=False)
    else:
        c=cancelApp(user_serializer.data,dose)
        if c == True:
            post_data={dose:None,dose+"_place":None,dose+"_date":None,dose+"_slot":None}
            post_data["register_number"]=user_serializer.data["register_number"]
            post_data["user"]=user_serializer.data["user"]
            user_serializer= userSerializer(user_data,data=post_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse({'status':200,'response':"Successfully cancelled appointment"}, safe=False)
            return JsonResponse({'status':400,'response':"Failed to update!"}, safe=False)
        return JsonResponse({'status':200,'response':"Nothing to cancel"}, safe=False)


def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) <(birthDate.month, birthDate.day))
 
    return age

def validateDate(needdate,dose,first_dose_date):
    date_object = datetime.strptime(needdate, '%Y-%m-%d')
    today = datetime.now()
    d = timedelta(days = 90)
    a = today + d
    if dose == "first_dose":
        if((date_object) < (a) and (date_object) > (today)):
            return (True,"Date is valid to register")
        else:
            return  (False,"Please enter a date within 90 days from today!")
    else:
        second_date_obj = datetime.strptime(first_dose_date, '%Y-%m-%d')
        d = timedelta(days = 15)
        s = second_date_obj + d
        if((date_object) < (a) and (date_object) > (s)):
            return (True,"Date is valid to register")
        else:
            return  (False,"Please enter a date within 90 days and after 15 days of vaccination!")


def findDose(data):
    if(data["first_dose_place"]==None):
        return("first_dose")
    elif(data["first_dose"]==True and data["second_dose_place"]==None):
        return("second_dose")
    else:
        pass
    return None

def findSlot(data):
    slot={"9.30amto11.30am":"slot_one","2pmto4pm":"slot_two","6pmto8pm":"slot_three"}
    if data["slot"] in slot:
        return(slot[data["slot"]])
    else:
        pass
    return None
def FindPlace(slot,v_date,dose):
    place={ "Nungambakkam" : [placeOne,placeOneSerializer], "Tambaram": [placeTwo,placeTwoSerializer], "Velachery": [placethree,placethreeSerializer], "Shozhinganallur": [placeFour,placeFourSerializer]}
    for k,v in place.items():
        if v[0].objects.filter(vaccination_date=v_date).exists():
            place_object=placeOne.objects.get(vaccination_date=v_date)
            place_serializer = v[1](place_object,many=False)
            if(place_serializer.data[dose]+1 <= 15):
                if(place_serializer.data[slot]+1 <= 10):
                    f=place_serializer.data[dose]+1
                    s=place_serializer.data[slot]+1 
                    data1={"vaccination_date":v_date,slot:s,dose:f}
                    place_serializers= v[1](place_object,data=data1)
                    if place_serializers.is_valid():
                        place_serializers.save()
                        return(k)                  
        else:
            data1={"vaccination_date":v_date,slot:1,dose:1}
            place_serializers= v[1](data=data1)
            if place_serializers.is_valid():
                place_serializers.save()
                return(k)
def postUserData(dose,slot,place,date):
    data={}
    if dose == "first_dose":
        data['first_dose_place'] = place
        data['first_dose_slot'] = slot
        data['first_dose_date'] = date
    else:
        data['second_dose_place'] = place
        data['second_dose_slot'] = slot
        data['second_dose_date'] = date  
    return data     

def findDoseStatus(data):
    if(data["first_dose_place"]!=None and data["first_dose"]== None):
        return("first_dose")
    elif(data["second_dose_place"]!=None and data["second_dose"]== None):
        return("second_dose")
    else:
        pass
    return None   

def cancelApp(data,dose):
    place={ "Nungambakkam" : [placeOne,placeOneSerializer], "Tambaram": [placeTwo,placeTwoSerializer], "Velachery": [placethree,placethreeSerializer], "Shozhinganallur": [placeFour,placeFourSerializer]}
    v_place=data[dose+"_place"]
    v_date=data[dose+"_date"]
    slot=data[dose+"_slot"]
    v_center=place[v_place]
    place_object=v_center[0].objects.get(vaccination_date=v_date)
    place_serializer = v_center[1](place_object,many=False)
    f=place_serializer.data[dose]-1
    s=place_serializer.data[slot]-1
    data1={"vaccination_date":v_date,slot:s,dose:f}
    place_serializers= v_center[1](place_object,data=data1)
    if place_serializers.is_valid():
        place_serializers.save()
        return(True)
    return False