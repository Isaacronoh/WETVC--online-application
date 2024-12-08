from urllib import request
from django.shortcuts import render, redirect,get_object_or_404
from .models import Slider,Card1,Card2,Card3,Application,Course,Staff,Student,Finance,Result, User
from onlineapp.models import Status
from django.contrib import messages
from . serializers import ApplicationSerializer
from rest_framework import viewsets
from django.db.models import Q,Sum
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
# trial import 
from django.contrib.auth import authenticate, login, logout
from .forms import ResultForm,ApplicationForm 
from django.http import HttpResponse


# online application
def apply(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        id_number = request.POST.get('id number')
        postal_address = request.POST.get('adress')
        primary_school = request.POST.get('name-primary')
        primary_grade = request.POST.get('grade-primary')
        primary_year = request.POST.get('Year-primary')
        secondary_school = request.POST.get('name-secondary')
        secondary_grade = request.POST.get('grade-secondary')
        secondary_year = request.POST.get('Year-secondary')
        course = request.POST.get('course')
        level = request.POST.get('level')
        year_of_admission = request.POST.get('year_of_admission')
        intake = request.POST.get('intake')
        photo = request.FILES.get('photo')

        application = Application(
            name=name,
            gender=gender,
            email=email,
            phone=phone,
            id_number=id_number,
            postal_address=postal_address,
            primary_school=primary_school,
            primary_grade=primary_grade,
            primary_year=primary_year,
            secondary_school=secondary_school,
            secondary_grade=secondary_grade,
            secondary_year=secondary_year,
            course=course,
            level=level,
            year_of_admission=year_of_admission,
            intake=intake,
            photo=photo
        )
        application.save()
        messages.success(request, 'Application has been submitted successfully. Thank you!')

    return render(request, 'onlineapplication.html')

def application_list(request):
    applications = Application.objects.all()
    return render(request, 'application_list.html', {'applications': applications})

def about_us(request):
    return render(request, 'about_us.html')

def stafflogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and hasattr(user, 'staff'):
            login(request, user)
            return redirect('staffdashboard')  # Redirect to the staff dashboard
        else:
            messages.error(request, "Invalid credentials or you are not a staff member.")
            return render(request, 'stafflogin.html')

    return render(request, 'stafflogin.html')

def studentlogin(request):
    return render(request, 'studentlogin.html')

def courses(request):
    return render(request, 'courses.html')

def dashboard(request):
    # Ensure that the user is authenticated before fetching the student data
    if request.user.is_authenticated:
        try:
            student = Student.objects.get(adm_number=request.user.username)  # Assuming the admission number is used as the username
            context = {'student': student}
        except Student.DoesNotExist:
            student = None
            context = {'student': student}
        
        return render(request, 'student_dashboard.html', context)
    else:
        # Redirect to login page if the user is not authenticated
        return redirect('login')

@login_required
def staffdashboard(request):
    try:
        staff = Staff.objects.get(user=request.user)
    except Staff.DoesNotExist:
        staff = None
    
    context = {
        'staff': staff,
    }
    return render(request, 'staffdashboard.html', context)


    
    #home
     
def home(request):
    slider = Slider.objects.all()  
    card1 = Card1.objects.first()
    card2 = Card2.objects.first()
    card3 = Card3.objects.first()
    status = Status.objects.first()  
    if not status:
        context = {
            'attachment': 0,
            'session': 0,
            'graduated': 0,
        }
    else:
        context = {
            'attachment': status.attachment,
            'session': status.session,
            'graduated': status.graduated,
        }
    context['slider']= slider
    context['card1']= card1
    context['card2'] = card2
    context['card3'] = card3
    return render(request, 'home.html', context)

# view application

class ApplicationView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

def search(request):
    query= request.GET.get('search')
    if query:
        courses = Course.objects.filter(Q(course_name__icontains=query) | Q(code__icontains = query))
        return render(request, 'search.html',{'courses' : courses})
    return render(request, 'courses.html')

# register new student to login
def studentregistration(request):
  if request.method == 'POST':
    full_name = request.POST.get('full_name')
    adm_number = request.POST.get('adm_number')
    id_number = request.POST.get('id_number')  # Access id_number from POST data
    course = request.POST.get('course')
    yoa = request.POST.get('yoa')
    profile_pic = request.FILES.get('profile_pic') 

    # Create the User
    user = User.objects.create_user(
      username=adm_number,
      password=id_number,
      first_name=full_name
    )
    user.save()

    # Create the Student record (removed unnecessary id_number argument)
    student = Student.objects.create(
      full_name=full_name,
      adm_number=adm_number,
      id_number= id_number,
      course=course,
      yoa=yoa,
      profile_pic=profile_pic  # Save uploaded file
    )
    student.save()
    
    return redirect('studentlogin')
  
  return render(request, 'studentregistration.html')


# staff registartion

def staffregistration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        staff_number = request.POST.get('staff_number')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'staffregistration.html')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        
        Staff.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            staff_number=staff_number
        )

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('stafflogin')

    return render(request, 'staffregistration.html')



# login successfuly try
def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log in the user
            return redirect('student_dashboard')  # Redirect to dashboard
        else:
            messages.error(request, 'Invalid username or password')  # Display error

    return render(request, 'studentlogin.html')  # Render login form

def student_dashboard(request):
    return render(request, 'student_dashboard.html')


# finance section

def finance(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Ensure user is logged in

    finance = Finance.objects.filter(student=request.user).first()
    if not finance:
        return render(request, 'finance.html', {
            'error': "No financial records found for the logged-in student."
        })

    context = {
        'total_billed': finance.total_billed,
        'total_paid': finance.total_paid,
        'balance': finance.balance,
    }
    return render(request, 'finance.html', context)


# academics section

@login_required
def staff_enter_results(request):
    if not hasattr(request.user, 'staff'):
        return redirect('stafflogin')

    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staffdashboard')
    else:
        form = ResultForm()

    return render(request, 'staff_enter_results.html', {'form': form})

@login_required
def staff_edit_results(request, result_id):
    if not hasattr(request.user, 'staff'):
        return redirect('stafflogin')

    result = get_object_or_404(Result, id=result_id)

    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('staffdashboard')
    else:
        form = ResultForm(instance=result)

    return render(request, 'staff_edit_results.html', {'form': form, 'result': result})

def logout(request):
    
    return redirect('home')

def student_view_results(request):
    if not request.user.is_authenticated:
        return redirect('student_views_results')
    # Fetch results for the logged-in student
    results = Result.objects.filter(student=request.user)
    # Calculate total marks
    total_marks = results.aggregate(total=Sum('marks'))['total'] or 0

    return render(request, 'student_view_results.html', {
        'results': results,
        'total_marks': total_marks
    })

def application_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        applications = Application.objects.filter(
            name__icontains=search_query
        ) | Application.objects.filter(
            id_number__icontains=search_query
        )
    else:
        applications = Application.objects.all()

    return render(request, 'application_list.html', {'applications': applications})

def edit_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('application_list')  # Redirect to the list view after saving
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'edit_application.html', {'form': form})

# View to delete an application
def delete_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        application.delete()
        return redirect('application_list')  # Redirect to the list view after deletion
    return render(request, 'delete_application.html', {'application': application})

def staff_personal_info(request):
    return render(request, 'staff_personal_info.html')

def staff_view_results(request):
    return render(request, 'staff_view_results.html')

def staff_view_results(request):
   
    subjects = []
    results = [
       
    ]
    return render(request, 'staff_view_results.html', {'subjects': subjects, 'results': results})