from django.views.generic.base import TemplateView, View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from forms import UserCreateForm


class HomePageView(TemplateView):

    template_name = "base.html"


class CreteUserAndLogin(View):
    form_class = UserCreateForm
    initial = {}
    template_name = 'registration.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,  self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.clean_username()
            password = form.clean_password2()
            form.save()
            user = authenticate(username=username,
                                password=password)
            login(request, user)

            return HttpResponseRedirect('/index/')

        return render(request, self.template_name, {'form': form})


class AjaxView(TemplateView):

    template_name = "ajax.html"