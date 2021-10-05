from django.http import request
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .forms import UserRegistration, UserEditForm
from .helpers import SomeHelper


@login_required
def dashboard(request):
    some_helper = SomeHelper()
    some = some_helper.some_work(request)
    context = {
        'helper':some,
    }
    return render(request, 'log_in/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'log_in/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }
    return render(request, 'log_in/register.html', context=context)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'log_in/edit.html', context=context)

def navbar(request):
    # some_helper = SomeHelper()
    # some = some_helper.some_work(request)
    # context = {
    #     'helper':some,
    # }
    return render(request, 'base/navbar.html', {'lol':'lol'})





