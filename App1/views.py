from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
from App1.models import tb1,tb2

in1 = ""
in2 = ""

def last_update1(date, time):
    global in1,in2
    years1_in_seconds = 31536000*int(str(datetime.today().strftime("%Y-%m-%d")[0:4]))
    years2_in_seconds = 31536000*int(date[0:4])
    months1_in_seconds = 2592000*int(str(datetime.today().strftime("%Y-%m-%d")[5:7]))
    months2_in_seconds = 2592000*int(date[5:7])
    days1_in_seconds = 86400*int(str(datetime.today().strftime("%Y-%m-%d")[8:10]))
    days2_in_seconds = 86400*int(date[8:10]) 
    hours1_in_seconds = 3600*int(str(datetime.now().strftime("%H:%M:%S"))[0:2])
    hours2_in_seconds = 3600*int(time[0:2])
    minutes1_in_seconds = 60*int(str(str(datetime.now().strftime("%H:%M:%S"))[3:5]))
    minutes2_in_seconds = 60*int(time[3:5])
    seconds1 = int(str(datetime.now().strftime("%H:%M:%S"))[6:8])
    seconds2 = int(time[6:8])
    actual_time_in_seconds = years1_in_seconds + months1_in_seconds + days1_in_seconds + hours1_in_seconds + minutes1_in_seconds + seconds1
    last_update_time = years2_in_seconds + months2_in_seconds + days2_in_seconds + hours2_in_seconds + minutes2_in_seconds + seconds2
    difference_in_seconds = actual_time_in_seconds - last_update_time
    if difference_in_seconds/31536000 >= 1:
        if int(difference_in_seconds/31536000) == 1:
            in1 = "year"
        else:
            in1 = "years"   
        return str(int(difference_in_seconds/31536000))
    elif difference_in_seconds/2678400 >= 1:
        if int(difference_in_seconds/2678400) == 1:
            in1 = "month"
        else:
            in1 = "months"    
        return str(int(difference_in_seconds/2678400))
    elif difference_in_seconds/604800 >= 1:
        if int(difference_in_seconds/604800) == 1:
            in1 = "week"
        else:
            in1 = "weeks"
        return str(int(difference_in_seconds/604800))
    elif difference_in_seconds/86400 >= 1:
        if int(difference_in_seconds/86400) == 1:
            in1 = "day"
        else:
            in1 = "days"         
        return str(int(difference_in_seconds/86400))
    elif difference_in_seconds/3600 >= 1:
        if int(difference_in_seconds/3600) == 1:
            in1 = "hour"
        else:
            in1 = "hours"
        return str(int(difference_in_seconds/3600))
    elif difference_in_seconds/60 >= 1:
        if int(difference_in_seconds/60) == 1:
            in1 = "minute"
        else:
            in1 = "minutes"    
        return str(int(difference_in_seconds/60))
    else:
        if int(difference_in_seconds) == 1:
            in1 = "seconde"
        else:
            in1 = "seconds"    
        return str(int(difference_in_seconds))

def last_update2(date, time):
    global in1,in2
    years1_in_seconds = 31536000*int(str(datetime.today().strftime("%Y-%m-%d")[0:4]))
    years2_in_seconds = 31536000*int(date[0:4])
    months1_in_seconds = 2592000*int(str(datetime.today().strftime("%Y-%m-%d")[5:7]))
    months2_in_seconds = 2592000*int(date[5:7])
    days1_in_seconds = 86400*int(str(datetime.today().strftime("%Y-%m-%d")[8:10]))
    days2_in_seconds = 86400*int(date[8:10]) 
    hours1_in_seconds = 3600*int(str(datetime.now().strftime("%H:%M:%S"))[0:2])
    hours2_in_seconds = 3600*int(time[0:2])
    minutes1_in_seconds = 60*int(str(str(datetime.now().strftime("%H:%M:%S"))[3:5]))
    minutes2_in_seconds = 60*int(time[3:5])
    seconds1 = int(str(datetime.now().strftime("%H:%M:%S"))[6:8])
    seconds2 = int(time[6:8])
    actual_time_in_seconds = years1_in_seconds + months1_in_seconds + days1_in_seconds + hours1_in_seconds + minutes1_in_seconds + seconds1
    last_update_time = years2_in_seconds + months2_in_seconds + days2_in_seconds + hours2_in_seconds + minutes2_in_seconds + seconds2
    difference_in_seconds = actual_time_in_seconds - last_update_time
    if difference_in_seconds/31536000 >= 1:
        if int(difference_in_seconds/31536000) == 1:
            in2 = "year"
        else:
            in2 = "years"   
        return str(int(difference_in_seconds/31536000))
    elif difference_in_seconds/2678400 >= 1:
        if int(difference_in_seconds/2678400) == 1:
            in2 = "month"
        else:
            in2 = "months"    
        return str(int(difference_in_seconds/2678400))
    elif difference_in_seconds/604800 >= 1:
        if int(difference_in_seconds/604800) == 1:
            in2 = "week"
        else:
            in2 = "weeks"
        return str(int(difference_in_seconds/604800))
    elif difference_in_seconds/86400 >= 1:
        if int(difference_in_seconds/86400) == 1:
            in2 = "day"
        else:
            in2 = "days"         
        return str(int(difference_in_seconds/86400))
    elif difference_in_seconds/3600 >= 1:
        if int(difference_in_seconds/3600) == 1:
            in2 = "hour"
        else:
            in2 = "hours"
        return str(int(difference_in_seconds/3600))
    elif difference_in_seconds/60 >= 1:
        if int(difference_in_seconds/60) == 1:
            in2 = "minute"
        else:
            in2 = "minutes"    
        return str(int(difference_in_seconds/60))
    else:
        if int(difference_in_seconds) == 1:
            in2 = "seconde"
        else:
            in2 = "seconds"    
        return str(int(difference_in_seconds))

def index(request):
    global in1,in2
    if tb1.objects.count() > 0 and tb2.objects.count() > 0:
        D1 = tb1.objects.last()
        D2 = tb2.objects.last()
        diff1 = last_update1(str(D1.Date), str(D1.Time))                
        diff2 = last_update2(str(D2.Date), str(D2.Time))        
        context = {"Data1": D1, "Data2": D2, "difference1": diff1, "index1": in1, "difference2": diff2, "index2": in2}
        return render(request, "index.html", context)
    else:
        return HttpResponse("<h1>Data are not avalaible</h1>") 
          
