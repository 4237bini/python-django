from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import UserProfileForm
from account.models import UserProfile
from django.core.files.storage import FileSystemStorage




# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']

        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('loginPage')

    else:
        return render(request, 'loginPage.html')












def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        passwordRepeat = request.POST['passwordRepeat']

        if password==passwordRepeat:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                print('user created')
                return redirect('loginPage')
        else:
            print('password not matching..')
            return redirect('register')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('home')




def adduserprofile(request, id):
    
    

    if request.method == 'POST':

        #user = User.objects.get(id = id)
        form = UserProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
          data = UserProfile()  # create relation with model
           # Access User Session information
          data.firstname = form.cleaned_data['firstname']
          data.lastname = form.cleaned_data['lastname']
          data.email = form.cleaned_data['email']
          data.phone = form.cleaned_data['phone']
          data.address = form.cleaned_data['address']
          data.experience = form.cleaned_data['experience']
          data.profession = form.cleaned_data['profession']
          data.total = form.cleaned_data['total']
          data.description = form.cleaned_data['description']
          data.profileimage = form.cleaned_data['profileimage']
          current_user = request.user
          data.user_id = current_user.id

          data.save()  # save data to table
          messages.info(request, "Your profile has been created. Thank you for your interest!!!")
          return redirect('userprofilecreated')
         

        else:
            
            return redirect('userprofile')
    return render(request, 'profile.html')    


    
     

def userprofilecreated(request, id):

    userprofile = UserProfile.objects.get(user_id = id)
    userdetail = UserProfile.objects.filter(user_id = id, status=True)
    context = {'userprofile':userprofile,
                'userdetail':userdetail}

    return render(request, 'profilecr.html',context) 

