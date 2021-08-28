from django.urls import path
from . import views
from .views import (
    MyProfile,
    ProfileData,
    # RegisterPage,
)


urlpatterns = [
    path('', views.all_profiles, name='profiles'),
    path('my_profile/', MyProfile.as_view(), name='my_profile'), # .as_view() to "convert" a class-based view for url
    path('profile_data/', ProfileData.as_view(), name='profile_data'), # .as_view() to "convert" a class-based view for url
    path('profile_details/', views.profile_details, name='profile_details'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('create_gig/', views.create_gig, name='create_gig'),

    path('register/', views.Register, name='register'),
    # path('register_profile/', views.RegisterPage, name='register_profile'),
    path('register_1/', views.ProfileForm1, name='register_1'),
    path('register_2/', views.ProfileForm2, name='register_2'),
    path('register_3/', views.ProfileForm3, name='register_3'),

    path('login/', views.loginPage, name='login'),
    path('terms/', views.terms, name='terms'),


    path('my_gigs/', views.my_gigs, name='my_gigs'),
    path('my_contacts/', views.my_contacts, name='my_contacts'),



]
