from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import re
@login_required
def home(request):
    if(request.method == 'POST'):
        text = request.POST["input"]
        option=request.POST.get("text-format")
        output=""
        if(option=='op1'):
            for i in text:
                if(i.isdigit()):
                    output+=str(i)
        elif(option=='op2'):
            syn = re.compile(r'\b\d{4}[\-\\/]((1[012])|(0?[1-9]))[\-\\/]((3[01])|([12][0-9])|([1-9]))\b')
            dates=syn.finditer(text)
            for i in dates:
                output+=i[0]+"\n"
        elif(option=='op3'):
            check=0;st=""
            for i in text:
                if(i=="'" and check==1):
                    output=st
                    break
                elif(i=="'"and check==0):
                    check=1
                elif(check==1):
                    st+=i
        elif(option=='op4'):
            syn=r"^(https?:\/\/)?(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){2}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
            if(re.search(syn,text)):
                output="Valid IP address"
                reg=re.compile(syn)
                matches=reg.finditer(text)
                for i in matches:
                    if(int(i.group(2))>=0 and int(i.group(2))<=127):
                        output+="\n Class A"
                    elif(int(i.group(2))>=128 and int(i.group(2))<=191):
                        output+="\n Class B"
                    elif(int(i.group(2))>=192 and int(i.group(2))<=223):
                        output+="\n Class C"
                    elif(int(i.group(2))>=224 and int(i.group(2))<=239):
                        output+="\n Class D"
                    elif(int(i.group(2))>=240 and int(i.group(2))<=255):
                        output+="\n Class E"
            else:
                output="Invalid IP address"
        elif(option=='op5'):
            syn="^[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+$"
            if(re.search(syn,text)):
                output="Valid Email"
            else:
                output="Invalid Email"
        elif(option=='op6'):
            syn = r"^(([0-9a-fA-F]{2}[.:-]){5}([0-9a-fA-F]{2}))|(([0-9a-fA-F]{4}[.:-])([0-9a-fA-F]{4}[.:-])([0-9a-fA-F]{4}))$"
            if(re.search(syn,text)):
                output="Valid Mac Address"
            else:
                output="Invalid Mac Address"
        elif(option=='op7'):
            syn=re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
            output=re.sub('([a-z0-9])([A-Z])', r'\1_\2', syn).lower()
        return render(request,'rc/home.html',{'output':output,'input':text})
    return render(request, 'rc/home.html',{'input':""})