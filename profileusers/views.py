from .models import Profileuser
from .forms import ProfileForm, RegisterUserForm, ProfileForm1, ProfileForm2, ProfileForm3

from django.core import serializers
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetDoneView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.db.models.functions import Lower
from django.db.models.query_utils import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View


# PASSWORD USAGE

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    #template_name = 'profileusers/password_change.html'
    success_url = reverse_lazy('password_success')
    #success_url = reverse_lazy('profile_details')


def PasswordSuccess(request):
    return render(request, 'profileusers/password_success.html', {})


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'profileusers/password_reset_done.html'


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "profileusers/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'https://biz-net.herokuapp.com',
					'site_name': 'BizNet',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
                        # send_mail(subject, contact_message, from_email, to_email, fail_silently = True)
						send_mail(subject, email, [user.email], fail_silently=True) #  'AWS_verified_email_address',
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
						
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("main:homepage")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="profileusers/password_reset.html", context={"password_reset_form":password_reset_form})


# REGISTRATION & LOGIN

"""
class RegistrationView(View):
    def get (det, request):
        return render(request, 'signup.html')

    def post(self, request):

        messages.success(request, 'Success whatsapp success')
        return render(request, 'signup.html')

    def post (self, request):
        # Get user data
        # Validate
        # create a user account

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

"""
def Register(request):
    # pylint: disable=maybe-no-member
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_register_page')
    else:
        form = RegisterUserForm()

    context = {
        'form' : form
    }
    return render(request, 'profileusers/register.html', context)


def terms(request):
    # pylint: disable=maybe-no-member
    template = 'profileusers/terms.html'

    return render(request, template)


@login_required
def Profile(request):
    # profile_form1 = ProfileForm1()
    if request.method == 'POST':
        profile = Profile(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if profile.is_valid():
            profile.save()
            # messages.success(request, 'Step 1 of 3 done of creating your profile!')
            return redirect('register_1')
        # else:
            # messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profile = Profileuser.objects.create(username=request.user)
        # profile_form1 = ProfileForm1(instance=request.user.profileuser)
        # return redirect('register_1')
    context = {
        'profile':profile,
    }
    return render(request, 'profileusers/profile.html', context)
    

def ProfileOne(request):
    profile_form1 = ProfileForm1()
    if request.method == 'POST':
        profile_form1 = ProfileForm1(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if profile_form1.is_valid():
            profile_form1.save()
            # messages.success(request, 'Step 1 of 3 done of creating your profile!')
            # return redirect('register_2')
        # else:
            #messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        # profile_form1 = Profileuser.objects.create(user=request.user)
        profile_form1 = ProfileForm1(instance=request.user.profileuser)
    context = {
        'profile_form1':profile_form1,
    }
    return render(request, 'profileusers/register_1.html', context)


def ProfileTwo(request):
    if request.method == 'POST':
        profile_form2 = ProfileForm2(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if profile_form2.is_valid():
            profile_form2.save()
            # messages.success(request, 'Step 2 of 3 done of creating your profile!')
            # return redirect('register_3')
        #else:
            # messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profile_form2 = ProfileForm2(instance=request.user.profileuser)
    context = {
        'profile_form2':profile_form2,
    }
    return render(request, 'profileusers/register_2.html', context)


def ProfileThree(request):
    if request.method == 'POST':
        profile_form3 = ProfileForm3(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if profile_form3.is_valid():
            profile_form3.save()
            # messages.success(request, 'Step 3 of 3 done of creating your profile!')
            # return redirect('profile_details')
        # else:
            # messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profile_form3 = ProfileForm3(instance=request.user.profileuser)
    context = {
        'profile_form3' : profile_form3
    }
    return render(request, 'profileusers/register_3.html', context)

"""
@login_required
def RegisterPage(request):
    profile_form = EditForm()
    if request.method == 'POST':
        profile_form = EditForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user # Profileuser.objects.create(user=instance)
            
            profile_form.save()
            # messages.success(request, 'Your Profile has been updated!')
            return redirect('login')
        # else:
            # messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profile_form = EditForm()

    context = {
        'profile_form' : profile_form
    }
    return render(request, 'profileusers/register_profile.html', context)
"""

# SINGIN TO ACCOUNT
def loginPage(request):
    if request.method == 'POST':
        # Connected to the name field in the login_page.
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_details')
        else:
            # messages.info(request, 'Username or Password is incorrect!')
            return redirect('login_page')
  
    template = 'profileusers/login_page.html'
    context = {}
    return render(request, template, context)


def loginRegisterPage(request):
    if request.method == 'POST':
        # Connected to the name field in the login_page.
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Username or Password is incorrect!')
            
    template = 'profileusers/login_register_page.html'
    context = {}
    return render(request, template, context)


# PROFILES

# @login_required
def profile_details(request):
    # pylint: disable=maybe-no-member
    #profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(username=request.user)
    template = 'profileusers/profile_details.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        if profileform.is_valid():
            profileform.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile_details')
        else:
            messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profileform = ProfileForm(instance=request.user.profileuser)
    context = {
        'profileform':profileform,
        # 'on_profile_page': True
    }
    return render(request, 'profileusers/profile_edit.html', context)


"""
@login_required
def profile_edit(request):
    if request.method == 'POST':
        profile_form1 = ProfileForm1(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        profile_form2 = ProfileForm2(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)
        profile_form3 = ProfileForm3(request.POST, 
                                request.FILES, 
                                instance=request.user.profileuser)

        if profile_form1.is_valid() and profile_form2.is_valid() and profile_form3.is_valid():
            profile_form1.save()
            profile_form2.save()
            profile_form3.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('profile_details')
        else:
            messages.error(request, 'Update failed. Please check if your inputs are valid.')
    else:
        profile_form1 = ProfileForm1(instance=request.user.profileuser)
        profile_form2 = ProfileForm2(instance=request.user.profileuser)
        profile_form3 = ProfileForm3(instance=request.user.profileuser)
    context = {
        'profile_form1':profile_form1,
        'profile_form2':profile_form2,
        'profile_form3':profile_form3,
    }
    return render(request, 'profileusers/profile_edit.html', context)
"""

@login_required
def all_profiles(request):
    # pylint: disable=maybe-no-member
    profiles = Profileuser.objects.all()
    template = 'profileusers/all_profiles.html'
    context = {
        'profiles': profiles,
    }
    return render(request, template, context)


# MY GIGS

@login_required
def my_gigs(request):
    # pylint: disable=maybe-no-member
    # profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/my_gigs.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


@login_required
def create_gig(request):
    # pylint: disable=maybe-no-member
    #profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/create_gig.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


# CONTACTS

@login_required
def my_contacts(request):
    # pylint: disable=maybe-no-member
    # profile = get_object_or_404(Profileuser, user=request.user)
    profile = Profileuser.objects.get(user=request.user)
    template = 'profileusers/my_contacts.html'
   
    context = {
        'profile': profile,
        # 'get_following': get_following,
        # 'get_followers': get_followers,
    }
    return render(request, template, context)


# SUGGEST BUTTON OF PPL TO FOLLOW

# class for random contacts to add

class MyProfile(TemplateView):
    template_name = 'profileusers/profile_details.html'


class ProfileData(View):
    def get(self, *args, **kwargs): # , *args, **kwargs
        # pylint: disable=maybe-no-member
        profile = Profileuser.objects.get(user=self.request.user)
        qs = profile.get_proposal_contact()
        profile_to_follow_list = []
        for user in qs:
            # Select random profiles
            p = Profileuser.objects.get(user__username=user.username)
            # p = get_object_or_404(Profileuser, user__username=user.username)
            profile_item = {
                # 'id': p.id,
                'user': p.user.username,
                'firstname': p.firstname,
                'lastname': p.lastname,
                'avatar': p.avatar.url,
                'profession': p.profession,
                'company_name': p.company_name,
            }
            profile_to_follow_list.append(profile_item)
        return JsonResponse({'pf_data': profile_to_follow_list})
