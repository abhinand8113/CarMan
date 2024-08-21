from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Count
from.models import *
import razorpay


# Create your views here.


def index(request):
    return render(request,'index.html')

def reg_driver(request):
    return render(request,'driverregistration.html')

from.models import driver_reg
from.models import driver_login

def registration_driver(request):
    if request.method=='POST':
        a=request.POST['n1']
        b=request.POST['n2']
        c=request.POST['n3']
        d=request.POST['n4']
        e=request.POST['n5']
        f=request.POST['n6']
        g=request.POST['n7']
        h=request.POST['n8']
        i=request.FILES['n9']
        j=request.POST['n10']
        k=request.POST['n11']
        l = request.POST['n12']

        if j==k:
            data = driver_reg.objects.create(Name=a, Username=b,DriverId=l, Email=c, Phone=d, Zip=e,City=f,State=g,Address=h,Licence=i,Password=j,Cnf_password=k,Status='Pending')
            data.save()
            data1 = driver_login.objects.create(Username=b, Password=j,Status='Pending')
            data1.save()
            return render(request,'driverlogin.html')

        else:
            messages.info(request,"Password missmatch")
            return render(request,'driverregistration.html')

def log_driver(request):
    return render(request,'driverlogin.html')

def home_driver(request):
    return render(request, 'driver_home.html')


def profile(request):
    if 'u_id' in request.session:
        return render(request,'user_booking.html')
    elif 'd_id' in request.session:
        return render(request,'driver_home.html')
    elif 'a_id' in request.session:
        return render(request,'admin_home.html')
    else:
        return render(request,'index.html')
def login_driver(request):
    if request.method=='POST':
        u=request.POST['n1']
        p=request.POST['n2']

        try:
            data=driver_login.objects.get(Username=u)
            print(data)
            request.session['d_name'] = data.Username
            if data.Status=='Pending':
                messages.info(request, "Approval is pending")
                return render(request, 'driverlogin.html')
            else:
                if data.Password==p:
                    request.session['d_id']=u
                    return redirect(profile)
                    data=drivertableshow.objects.filter(DriverId=u,Status='Pending')
                    return render(request,'driver_home.html',{'a':len(data)})
                else:
                    messages.info(request,"password is incorrect")
                    return render(request,'driverlogin.html')
        except Exception:
            messages.info(request, "username or password is incorrect")
            return render(request, 'driverlogin.html')
    else:
        return render(request,'driverlogin.html')

def logout(request):
    if 'd_id' in request.session:
        request.session.flush()
        return redirect(index)
    elif 'u_id' in request.session:
        request.session.flush()
        return redirect(index)
    elif 'a_id' in request.session:
        request.session.flush()
        return redirect(index)


from.models import user_reg
from.models import user_login

def reg_user(request):
    return render(request,'userregistration.html')

def registration_user(request):
    if request.method=='POST':
        a=request.POST['Name']
        b=request.POST['Username']
        c=request.POST['Email']
        d=request.POST['Phone']
        e=request.POST['Password']
        f=request.POST['Cpassword']
        g=request.POST['User_id']
        if e==f:
            data=user_reg.objects.create(Name=a,Username=b,UserId=g,Email=c,Phone=d,Password=e,Cnf_password=f)
            data.save()
            data1=user_login.objects.create(Username=b,Password=e)
            data1.save()
            return render(request,'userlogin.html')
        else:
            messages.info(request,"password mismatch")
            return render(request, 'userregistration.html')

def login_user(request):
    return render(request,'userlogin.html')


def loginuser(request):
    if request.method=='POST':
        x=request.POST['username']
        y=request.POST['password']
        try:
            data = user_login.objects.get(Username=x)
            if data.Password==y:
                request.session['u_id']=x
                return redirect(profile)
            else:
                messages.info(request,"password is incorrect")
                return render(request,'userlogin.html')
        except Exception:
            messages.info(request,"Username or Password in Incorrect")
            return render(request,'userlogin.html')
    else:
        return render(request,'userlogin.html')

def userbooking(request):
    return render(request,'user_booking.html')

def oneway_trip(request):
    if request.method=='POST':
        a=request.POST['name']
        b=request.POST['date']
        c=request.POST['sl']
        d=request.POST['el']
        e=request.POST['phone']
        s='no driver'
        UserId=request.session['u_id']
        data=one_way.objects.create(Name=a,Date=b,StartingL=c,EndingL=d,Phone=e,Type='Oneway')
        data.save()
        d1 = drivertableshow.objects.create(Name=a, Starting=c, Ending=d, Date=b,Phone=e,UserId=UserId,DriverId=s, Type='Oneway',Status='Pending')
        d1.save()
        return HttpResponse("<script>alert('Driver will contact you soon');window.location='/userbooking';</script>")

def twoway_trip(request):
    if request.method=='POST':
        a=request.POST['name']
        b=request.POST['date']
        c=request.POST['sl']
        d=request.POST['el']
        e=request.POST['phone']
        s = 'no driver'
        UserId = request.session['u_id']
        data=round_trip.objects.create(Name=a,Date=b,StartingL=c,EndingL=d,Phone=e,Type='RoundTrip')
        data.save()
        d1 = drivertableshow.objects.create(Name=a, Starting=c, Ending=d, Date=b, Phone=e,UserId=UserId,DriverId=s, Type='RoundTrip',Status='Pending')
        d1.save()
        return HttpResponse("<script>alert('Driver will contact you soon');window.location='/userbooking';</script>")

def package_trip(request):
    if request.method=='POST':
        a=request.POST['name']
        b=request.POST['destination']
        c=request.POST['sl']
        d=request.POST['sd']
        e=request.POST['ed']
        f=request.POST['days']
        g=request.POST['phone']
        h=int(f)*1000
        j=int(f)*100000
        s = 'no driver'
        request.session['amount']=h
        request.session['razor_amount'] = j
        UserId = request.session['u_id']
        data=package.objects.create(Name=a,Destination=b,StartingL=c,S_date=d,E_date=e,Days=f,Phone=g,Type='Package')
        data.save()
        d1=drivertableshow.objects.create(Name=a,Starting=c,Ending=b,UserId = UserId, DriverId = s,Date=d,Phone=g,Type='Package',Status='Pending')
        d1.save()
        return render(request,'booking_status.html')

def bookingstatus(request):
    return render(request,'booking_status.html')

def adminlogin(request):
    return render(request,'adminlogin.html')

def adminhome(request):
    d1 = driver_login.objects.filter(Status="Approve")
    d2 = user_login.objects.all()
    d3 = driver_reg.objects.filter(Status="Pending")
    d4 = drivertableshow.objects.all()
    return render(request, 'admin_home.html', {'driver': len(d1), 'user': len(d2), 'req': len(d3), 'trips': len(d4)})


def loginadmin(request):
    if request.method=='POST':
        x=request.POST['name']
        y=request.POST['Password']
        try:
            data=admin_login.objects.get(Username=x)
            if data.Password==y:
                request.session['a_id']=x
                d1 = driver_login.objects.filter(Status="Approve")
                d2=user_login.objects.all()
                d3=driver_reg.objects.filter(Status="Pending")
                d4=drivertableshow.objects.all()
                return render(request,'admin_home.html',{'driver':len(d1),'user':len(d2),'req':len(d3),'trips':len(d4)})
            else:
                messages.info(request, "Password is Incorrect")
                return render(request, 'adminlogin.html')
        except Exception:
            messages.info(request, "Username or Password in Incorrect")
            return render(request, 'adminlogin.html')
    else:
        return render(request,'adminlogin.html')

def table_accrej(request):
    x=driver_reg.objects.filter(Status='Pending')
    return render(request,'basic_table.html',{'a':x})

def driver_reject(request,n):
    if request.method=='GET':
        x=driver_reg.objects.filter(Username=n)
        x.delete()
        x1=driver_login.objects.filter(Username=n)
        x1.delete()
        return HttpResponse("<script>alert('Rejected Successfully');window.location='/table';</script>")

def driver_accept(request,n):
    if request.method=='GET':
        x=driver_reg.objects.filter(Username=n)
        x.update(Status="Approve")
        x1=driver_login.objects.filter(Username=n)
        x1.update(Status="Approve")
        return HttpResponse("<script>alert('Approved Successfully');window.location='/table';</script>")


def bookingstatus(request):
    return render(request,'booking_status.html')

def driver_table(request):
    return render(request,'driver_table.html')

def one(request):
    return render(request,'1.html')

def driver_accrejtable(request):
    y = request.session['d_id']
    z=driver_reg.objects.get(Username=y)
    x = drivertableshow.objects.filter(Status='Pending',Starting=z.City)
    return render(request, 'driver_table.html', {'a': x})

def trip_accept(request,n):
    if request.method=='GET':
        x=drivertableshow.objects.filter(id=n)
        y=request.session['d_id']
        x.update(Status="Approve",DriverId=y)
        return HttpResponse("<script>alert('Trip Approved');window.location='/driveraccrej';</script>")

def usertrips(request):
    return render(request, 'usertrips.html')

def cust_message(request):
    if request.method=='POST':
        name=request.POST['n1']
        message=request.POST['n2']
        mail=request.POST['n3']
        data=customer_message.objects.create(Name=name,Message=message,Email=mail)
        data.save()
        return HttpResponse("<script>alert('Response send Successfully, Our Team contact you soon');window.location='/index';</script>")


def usertrips_table(request):
    y=request.session['u_id']
    print(y)
    x=drivertableshow.objects.filter(UserId=y)
    print(x)
    return render(request,'usertrips.html',{'user_trips':x})

def inbox(request):
    return render(request,'inbox.html')

def inbox_messages(request):
    x=customer_message.objects.all()
    return render(request,'inbox.html',{'messages':x})



def payment(request, id):
    amount = request.session['razor_amount']
    order_currency = 'INR'
    client = razorpay.Client(
        auth=("rzp_test_1ggfesqSHVkHcQ", "z0jCd9GhTBQsAAbKdiHrLQc5"))
    x = package.objects.filter(id=id)
    x.update(Payment_status="Done")
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, "payment.html")

def paymentdone(request):
    return render(request,'payment.html')

def paymentcancelled(request):
    return render(request,'paymentcancelled.html')






