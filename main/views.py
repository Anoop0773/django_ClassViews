from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import  FormLogin
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.urls import reverse_lazy,reverse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from tasks.models import *
from projects.models import *
from django.contrib.auth.mixins import LoginRequiredMixin






# Create your views here.
class Login(FormView):
    form_class = FormLogin
    template_name = 'login.html'
    success_url = reverse_lazy('dashboard')

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())

        return super(Login, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        error = None
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        

        obj_user = authenticate(username=username, password=password)

        if obj_user is not None:
            if not obj_user.is_active:
                error = 'This user is inactive'
           
        else:
            error = 'unregistered user or wrong password'

        if not error:
            login(self.request, obj_user)
            return HttpResponseRedirect(self.get_success_url())
        return render_to_response(
            'login.html',
            {'form': self.form_class(), 'error': error}
        )

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))

class Dashboard(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'
    def get_context_data(self, *args, **kwargs):
        context = super(Dashboard, self).get_context_data(*args, **kwargs)
        
        context['total_tasks'] = Tasks.objects.filter(assigned_user = self.request.user).count()
        task_list = Tasks.objects.filter(assigned_user =  self.request.user).values_list('project').distinct()
        member_project_list =  [Projects.objects.filter(pk = int(task[0])) for task in task_list]
        context['total_projects'] = Projects.objects.filter(user = self.request.user).count() + len(member_project_list)
        return context

