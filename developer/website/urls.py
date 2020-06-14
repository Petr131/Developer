from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('blog/',views.blog,name='blog'),
    path('blog_details/',views.blog_details,name='blog_details'),
    path('elements/',views.elements,name='elements'),
    path('portfolio_details/',views.portfolio_details,name='portfolio_details'),
    path('contact/',views.contact,name='contact'),
]
