from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello. You're at the index page.")


def user_verify(request, student_id):
    return HttpResponse("This is the user verify page for student %d." % student_id)


def send_verify_email(request):
    return HttpResponse("This is the send verify email page.")


def verify_email(request, uid, verification_code):
    return HttpResponse("This is the verify email page. "
                        "The uid is %d. His verification code is %d" % uid % verification_code)


def get_course_ddls(request, course_id):
    return HttpResponse("This is the get course ddls page for course id %d." % course_id)


def get_user_ddls(request, uid):
    return HttpResponse("This is the get user ddls page for user id %d." % uid)


def get_all_ddls(request):
    return HttpResponse("This is the get all ddls page.")


def get_user_tasks(request, uid, tid):
    return HttpResponse("This is the get user tasks page for user id %d task id %d" % uid % tid)


def get_user_courses(request, uid):
    return HttpResponse("This is the get user courses page for user id %d" % uid)


def get_all_tasks(request):
    return HttpResponse("This is the get all tasks page.")


def apply_course(request, uid, course_id):
    return HttpResponse("This is the apply course page for user id %d course id %d" % uid % course_id)


def quit_course(request, uid, course_id):
    return HttpResponse("This is the quit course page for user id %d course id %d" % uid % course_id)


def set_alert(request, uid, tid):
    return HttpResponse("This is the set alert page for user id %d task id %d" % uid % tid)


def appoint_course_leader(request, course_id):
    return HttpResponse("This is the appoint course leader page for course id %d" % course_id)


def user_apply(request):
    return HttpResponse("This is the user apply page.")


def get_user_info(request, uid):
    return HttpResponse("This is the get user info page for user %d." % uid)


def modify_user_info(request, uid):
    return HttpResponse("This is the modify user info page for user %d." % uid)

