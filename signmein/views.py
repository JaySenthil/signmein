# signmein/views.py
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm, MeetingCreationForm, MeetingDeletionForm, SignInForm
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Meetings, CustomUser, Members
from django.template.defaultfilters import slugify

class LoginPageView(TemplateView):
    template_name = 'login.html'

def SignInPageView(request, orgname):
    userobj = CustomUser.objects.filter(orgNameUrl = orgname)
    if userobj:
        meetobj = Meetings.objects.filter(organization = userobj[0])
    else:
        return redirect('notfound')
    if meetobj:
        if request.method == "POST":
            form = SignInForm(request.POST)
            if form.is_valid():
                newatt = form.save(commit = False)
                newatt.orgRef = userobj[0]
                newatt.meetRef = meetobj[0]
                newatt.save()
                return render(request, 'success.html')
        else:
            form = SignInForm()
        return render(request, 'signin.html', {'form': form})
    else:
        return redirect('notfound')

def SuccessPageView(request, orgname):
    userobj = CustomUser.objects.filter(orgNameUrl = orgname)
    if userobj:
        meetobj = Meetings.objects.filter(organization = userobj[0])
    else:
        return redirect('notfound')
    if meetobj:
        return render(request, 'success.html')
    else:
        return redirect('notfound')

def NotFoundView(request):
    return render(request, 'notfound.html')

def SignUpPageView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            newuser = form.save(commit = False)
            newuser.orgNameUrl = slugify(form.cleaned_data['orgName'])
            newuser.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def DashboardPageView(request):
    meetobj = Meetings.objects.filter(organization = request.user)
    if meetobj:
        status = 'Meeting is ongoing!'
        meetingExists = True
        # Get list of members for this meeting
        memberList = Members.objects.filter(meetRef = meetobj[0])
    else:
        status = 'No meeting is being held currently.'
        meetingExists = False
        # set memberlist to empty array
        memberList = []
    # create form logic
    if request.method == "POST" and 'newmeet-form' in request.POST:
        form = MeetingCreationForm(request.POST)
        if form.is_valid():
            meeting = Meetings()
            meeting.organization = request.user
            meeting.save()
            return redirect('dash')
    else:
        form = MeetingCreationForm()
    # delete form logic
    if request.method == "POST" and 'delmeet-form' in request.POST:
        form_del = MeetingDeletionForm(request.POST)
        if form_del.is_valid():
            meetobj.delete()
            return redirect('dash')
    else:
        form_del = MeetingDeletionForm()
    return render(request, 'dash.html', {'form': form, 'form_del': form_del, 'status': status, 'meetingExists': meetingExists, 'memberList': memberList})
