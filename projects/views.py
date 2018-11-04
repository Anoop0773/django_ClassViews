from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
import json
from .models import *
from tasks.models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin






class ListProject(LoginRequiredMixin,ListView):
    model = Projects
    template_name = 'projects.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ListProject, self).get_context_data(*args, **kwargs)
        context['owner_project'] = Projects.objects.filter(user = self.request.user)
       
        task_list = Tasks.objects.filter(assigned_user =  self.request.user).values_list('project').distinct()
        member_project_list =  [Projects.objects.filter(pk = int(task[0])) for task in task_list]
        print(member_project_list)
        context['member_project'] = member_project_list
        return context


class DetailProject(LoginRequiredMixin,DetailView):
    model = Projects
    template_name = 'projectDetail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(DetailProject, self).get_context_data(*args, **kwargs)
        context['users'] = User.objects.exclude(username=self.request.user)
        context['tasks'] = Tasks.objects.filter(project = self.object)
        return context

class CreateProject(TemplateView):
    template_name = 'createProject.html'



def SaveProject(request):
    if request.is_ajax() and request.method == 'POST':
        data = {}
        project_pk = request.POST.get('project_pk', None)
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        start_date = request.POST.get('start_date', None)
        end_date = request.POST.get('end_date', None)
       
        if ((name is not None and name !="") and (description is not None and description != "") and (start_date is not None and start_date != "") and (end_date is not None and end_date != "")):
            
            if project_pk is None:
                project = Projects()
            else:
                project = get_object_or_404(Projects, pk=int(project_pk))
               
            
            project.name = name
            project.discription = description
            project.user = request.user
            project.start_date = start_date
            project.end_date = end_date
            project.save()
            

            data['changes'] = 1

        else:
            data['changes'] = 0
        
        return HttpResponse(json.dumps(data), content_type='application/json')
    

def GetProject(request):
    if request.is_ajax() and request.method == 'POST':
        project_pk = request.POST.get('project_pk', None)
        obj_project = get_object_or_404(Projects, pk=int(project_pk))
        data = {
            'name': obj_project.name,
            'description': obj_project.discription,
            'start_date': obj_project.start_date.strftime('%Y-%m-%d'),
            'end_date': obj_project.end_date.strftime('%Y-%m-%d')
            
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

def DeleteProject(request):
    if request.is_ajax() and request.method == 'POST':
        data = {}
        project_pk = request.POST.get('project_pk', None)
        print('project_pk',project_pk)
        Projects.objects.filter(pk=int(project_pk)).delete()
        data['changes'] = 1
        return HttpResponse(json.dumps(data), content_type='application/json')
        
