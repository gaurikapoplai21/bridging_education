from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='about_us-index'),
    path('FAQ',views.FAQ,name = 'about_us-FAQ'),
    path('ContactUs',views.ContactUs,name = 'about_us-ContactUs'),
    ]
