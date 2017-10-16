from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import user, student, event, grade, activitie, note
#from django.contrib.auth import logout
# Create your views here.

def dashboard(request):
    currentUser = get_object_or_404(user, employee_id=request.session["user"])
    context = {
        'currentUser': currentUser
    }
    return render(request, 'sapApp/dashboard.html', context)

def students(request):
    user_list = user.objects.all()
    student_list = student.objects.all().order_by('-sap_id').reverse()
    context = {
        'student_list': student_list,
        'user_list': user_list,
    }
    return render(request, 'sapApp/students.html', context)

def students2(request, sapID):
    currentStudent = get_object_or_404(student, sap_id=sapID)
    context = {
        'currentStudent': currentStudent
    }
    return render(request, 'sapApp/students2.html', context)

def sortIt(request):
    user_list = user.objects.all()
    if request.POST['sortby'] == '1':
        student_list = student.objects.all().order_by('-country').reverse()
    elif request.POST['sortby'] == '2':
        student_list = student.objects.all().order_by('-territory').reverse()
    elif request.POST['sortby'] == '3':
        student_list = student.objects.all().order_by('-last_name').reverse()
    elif request.POST['sortby'] == '4':
        student_list = student.objects.all().order_by('-group_number').reverse()
    else:
        student_list = student.objects.all().order_by('-sap_id').reverse()
    context = {
        'student_list': student_list,
        'user_list': user_list,
    }
    return render(request, 'sapApp/students.html', context)

def grades(request):
    return render(request, 'sapApp/grades.html')

def grades2(request):
    return render(request, 'sapApp/grades2.html')

def reports(request):
    return render(request, 'sapApp/reports.html')

def specificreport(request):
    return render(request, 'sapApp/specificreport.html')

def userProfile(request):
    currentUser = get_object_or_404(user, employee_id=request.session["user"])
    context = {
        'currentUser': currentUser
    }
    return render(request, 'sapApp/userprofile.html', context)

def loggedIn(request):
    if request.session["user"] > 0:
        currentUser = get_object_or_404(user, employee_id=request.session["user"])
        context = {
            'currentUser': currentUser
        }
        return render(request, 'sapApp/dashboard.html', context)
    if request.session["user"] == -1:
        return render(request, 'sapApp/login.html')

def signIn(request):
    userList = user.objects.all()
    for userTry in userList:
        if userTry.employee_id == int(request.POST['userName']):
            if userTry.user_password == request.POST['userPassword']:
                request.session["user"] = userTry.employee_id
    if request.session["user"] >= 0:
        currentUser = get_object_or_404(user, employee_id=request.session["user"])
        context = {
            'currentUser': currentUser
        }
        return render(request, 'sapApp/dashboard.html', context)
    else:
        request.session["user"] = -1
        return render(request, 'sapApp/login.html')

def newStudent(request):
    addingStudent = student(sap_id = int(request.POST['newSAP']), first_name = request.POST['newFirst'], last_name = request.POST['newLast'], email_address = request.POST['newEmail'], group_number = int(request.POST['newGroup']), territory = request.POST['newTerritory'], country = request.POST['newCountry'], employee_id = int(request.POST['newManager']), training_program = request.POST['newTraining'])
    addingStudent.save()
    user_list = user.objects.all()
    student_list = student.objects.all().order_by('-sap_id').reverse()
    context = {
        'student_list': student_list,
        'user_list': user_list,
    }
    return render(request, 'sapApp/students.html', context)

def signingUp(request):
    addingUser = user(employee_id = request.POST['employee_num'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], work_position = request.POST['work_position'], user_password = request.POST['password1'])
    addingUser.save()
    return render(request, 'sapApp/Signup.html')

def signUp(request):
    return render(request, 'sapApp/Signup.html')

def exitSession(request):
    request.session['user'] = -1
    return render(request, 'sapApp/login.html')