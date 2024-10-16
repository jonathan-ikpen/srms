from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    STUDY_MODE_CHOICES = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
    ]

    LEVEL_CHOICES = [
        ('ND1', 'ND Level 1'),
        ('ND2', 'ND Level 2'),
        ('HND1', 'HND Level 1'),
        ('HND2', 'HND Level 2'),
    ]

    HALL_CHOICES = [
        ('PTDF', 'PTDF'),
        ('NOBLE', 'Noble'),
        ('OLD', 'Old'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Academic Information
    matric_no = models.CharField(max_length=20, unique=True, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    directorate = models.CharField(max_length=100, null=True, blank=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(max_length=4, choices=LEVEL_CHOICES, null=True, blank=True)
    study_mode = models.CharField(max_length=2, choices=STUDY_MODE_CHOICES, null=True, blank=True)
    courses = models.ManyToManyField('Course', blank=True)
    course_scores = models.ManyToManyField('CourseScores', blank=True, related_name='student_course_scores')
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    tgp = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    result_remark = models.CharField(max_length=100, null=True, blank=True)
    gpa_first_semester = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    gpa_second_semester = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    attendance_percentage = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    # Personal Information
    surname = models.CharField(max_length=100, null=True, blank=True)
    other_names = models.CharField(max_length=100, null=True, blank=True)
    maiden_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    state_of_origin = models.CharField(max_length=100, null=True, blank=True)
    local_government_area = models.CharField(max_length=100, null=True, blank=True)
    home_address = models.TextField(null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    # Next of Kin
    marital_status = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_phone_number = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_address = models.TextField(null=True, blank=True)
    next_of_kin_relationship = models.CharField(max_length=100, null=True, blank=True)
    next_of_kin_email = models.EmailField(max_length=100, null=True, blank=True)
    hall_of_residence = models.CharField(max_length=100, choices=HALL_CHOICES, null=True, blank=True)
    room_number = models.CharField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    # Medical Record
    blood_group = models.CharField(max_length=100, null=True, blank=True)
    medical_condition = models.TextField(null=True, blank=True)
    blood_type = models.CharField(max_length=100, null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    current_medication = models.TextField(null=True, blank=True)
    height = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    # Other Information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"

    
class Course(models.Model):
    name = models.CharField(max_length=100)
    unit = models.IntegerField(null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class CourseScores(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    score = models.CharField(max_length=20, null=True)
    grade = models.CharField(max_length=20, null=True)

    def __str__(self):
         return f"{self.course.name}: {self.score}" 
    
    class Meta:
        verbose_name = "Course Score"
        verbose_name_plural = "Course Scores"
    




