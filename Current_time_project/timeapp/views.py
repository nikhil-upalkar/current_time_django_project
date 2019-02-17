from django.shortcuts import render
import datetime

# Create your views here.
def date_time_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = ''
    if h<12:
        msg = "Morning"
    elif h<16:
        msg = "Afternoon"
    elif h<22:
        msg = "Evening"
    else:
        msg = "Night"
    return render(request,'timeapptemp/index.html',context={'msg':msg,'date':date})

