from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout


# Create your views here.
def signup_view(request):
    if request.method =='POST':
        #do something
        form= UserCreationForm(request.POST)#access data from the form filled by the user
        if form.is_valid():
            #save the data to the database
            user = form.save()
            #log the user in
            login(request,user)#this logs in the user
            return redirect('articles:list')#using named urlpattern
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def login_view(request):
    if request.method=="POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            #get the user and log them in
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST: #used to redirect to where they had initially wanted to go
                return redirect(request.POST.get('next'))
            return redirect('articles:list')#this happens if there was no 'next'

    else:
        if request.user.is_authenticated:
            return redirect("articles:list")
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{'form':form})

def logout_view(request):
    if(request.method=="POST"):
        logout(request)
        return redirect('articles:list')
