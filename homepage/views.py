import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse, HttpResponse
from homepage.forms import FeedbackForm
from django.urls import reverse
from homepage.forms import FeedbackForm
from homepage.models import Feedback
from django.core import serializers
from catalog.management.commands.load_book_data import Command


# Create your views here.
def show_homepage(request):
    form = FeedbackForm()
    last_login = request.COOKIES.get('last_login', 'Default Value if last_login not found')
    
    context = {
        'name': request.user.username,
        'last_login': last_login,
        # 'last_feedback': request.session.get('last_feedback', 'Belum ada feedback yang diberikan'),
        'form': form,
        'isadmin': request.user.is_staff,
    }
    Command().handle()
    return render(request, "homepage.html", context)

@login_required(login_url='/authentication/login/')
def submit_feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponseRedirect(reverse('homepage:show_homepage'))
        # response = serializers.serialize('json',[new_feedback])
        # request.session['last_feedback'] = str(datetime.datetime.now())
    return HttpResponseBadRequest


def show_json(request):
    data = Feedback.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")