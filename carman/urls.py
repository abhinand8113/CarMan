"""
URL configuration for carman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.profile),
    path('index', views.index),
    # path('driverprofile', views.d_profile),
    path('driverregform',views.reg_driver),
    path('driverreg', views.registration_driver),
    path('driverlog',views.log_driver),
    path('login_driver', views.login_driver),
    path('driverhome', views.home_driver),
    path('logout', views.logout),
    path('userregform', views.reg_user),
    path('userreg', views.registration_user),
    path('userlogin', views.login_user),
    path('userlog', views.loginuser),
    # path('userprofile', views.u_profile),
    path('userbooking', views.userbooking),
    path('oneway', views.oneway_trip),
    path('round', views.twoway_trip),
    path('package', views.package_trip),
    path('adminhome', views.adminhome),
    path('adminlogin', views.adminlogin),
    path('loginadmin', views.loginadmin),
    path('table', views.table_accrej),
    path('reject/<n>', views.driver_reject),
    path('accept/<n>', views.driver_accept),
    path('bookingstatus', views.bookingstatus),
    path('drivertable', views.driver_table),
    path('1', views.one),
    path('driveraccrej', views.driver_accrejtable),
    path('tripaccept/<n>', views.trip_accept),
    path('usertrips', views.usertrips_table),
    path('usertrips_table', views.usertrips_table),
    path('messages', views.cust_message),
    path('inbox_messages', views.inbox_messages),
    path('inbox_messages', views.inbox_messages),
    path('payment', views.payment),
    path('paymentdone', views.paymentdone),

    # path('paypal-ipn/', views.paypal_ipn, name='paypal-ipn'),
    # path('payment_process', views.payment_process),
    # path(r'^paypal/', include('paypal.standard.ipn.urls')),
    # path('payment_process/$', views.payment_process, name='payment_process'),
    # path(r'^payment_done/$', TemplateView.as_view(template_name="template/paymentdone.html"), name='payment_done'),
    # path(r'^payment_canceled/$', TemplateView.as_view(template_name="template/paymentcancelled.html"), name='payment_canceled'),

]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)