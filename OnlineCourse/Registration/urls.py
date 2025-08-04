from django.urls import path
from .import views
app_name = 'Registration'
urlpatterns = [
   
    path('',views.index,name="index"),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('home/',views.home,name='home'),
    path('courses/',views.courses,name='courses'),
    path('courses1/',views.courses1,name='courses1'),
     path('courses2/',views.courses2,name='courses2'),
      path('courses3/',views.courses3,name='courses3'),
      path('contactus/',views.contactus,name='contactus'),
      path('enquiry/',views.enquiry,name='enquiry'),
       path('process_contactus/',views.process_contactus,name="process_contactus"),
       path('process_enquiry/',views.process_enquiry,name="process_enquiry"),
]