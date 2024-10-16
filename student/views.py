from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm
from .models import Student, CourseScores
from xhtml2pdf import pisa
from django.template import Context
from django.template.loader import get_template



# Create your views here.
def index_view(request):
     # Check if the user is authenticated
    if request.user.is_authenticated:
        return redirect('dashboard') 
    return render(request, 'index.html')

def register_view(request):
     # Check if the user is authenticated
    if request.user.is_authenticated:
        return redirect('dashboard') 
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
             # Create User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            # Create Student
            Student.objects.create(
                user=user,
                matric_no=form.cleaned_data['matric_no'],
                surname=form.cleaned_data['surname'],
                other_names=form.cleaned_data['other_names'],
                phone_number=form.cleaned_data['phone_number'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                gender=form.cleaned_data['gender'],
                nationality=form.cleaned_data['nationality'],
                state_of_origin=form.cleaned_data['state_of_origin'],
                local_government_area=form.cleaned_data['local_government_area'],
                home_address=form.cleaned_data['home_address'],
                marital_status=form.cleaned_data['marital_status'],
                profile_picture=form.cleaned_data['profile_picture'],
                hall_of_residence=form.cleaned_data['hall_of_residence'],
                department=form.cleaned_data['department'],
                faculty=form.cleaned_data['faculty'],
                level=form.cleaned_data['level'],
                study_mode=form.cleaned_data['study_mode']
            )
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
     # Check if the user is authenticated
    if request.user.is_authenticated:
        return redirect('dashboard') 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'dashboard'
            return redirect(next_url)

        else:
            error_message = "Invalid credentials"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')
    else:
        return redirect('dashboard')


# @login_required
# def dashboard_view(request):
#     return render(request, 'dashboard.html')

class DashboardView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'dashboard/index.html')
    

class MedicalRecordView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'dashboard/medical_record.html')
    
class ExamRecordView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        # Access the course scores directly from the Student model
        # course_scores = request.user.student.course_scores.all()
        course_scores = CourseScores.objects.filter(student=request.user) 

        context = {
            'course_scores': course_scores,
        }
        return render(request, 'dashboard/exam_record.html', context)
    

class PerformanceTrackView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'dashboard/performance_track.html')


class DownloadPDFView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        course_scores = CourseScores.objects.filter(student=request.user)
        context = {
            'course_scores': course_scores,
            'user': request.user,
        }
        template = get_template('dashboard/pdf_exam_record.html')  # Create this template
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="exam_record.pdf"'
        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

