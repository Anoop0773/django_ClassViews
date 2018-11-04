from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def SaveTask(request):
    if request.is_ajax() and request.method == 'POST':
        data = {}
        task_pk = request.POST.get('task_pk', None)
        name = request.POST.get('name', None)
        description = request.POST.get('description', None)
        user_pk = request.POST.get('user_pk', None)
        project_pk = request.POST.get('project_pk', None)
    
        
        if ((name is not None and name !="") and (description is not None and description != "") and (project_pk is not None and project_pk != "") and (user_pk is not None and user_pk != "")):
            
            if task_pk is None:
                task = Tasks()
            else:
                task = get_object_or_404(Tasks, pk=int(task_pk))
            task.name = name
            task.discription = description
            task.assigned_user = get_object_or_404(User,pk = int(user_pk))
            task.project = get_object_or_404(Projects,pk = int(project_pk))
            
            
            task.save()
            data['changes'] = 1

        else:
            data['changes'] = 0
        
        return HttpResponse(json.dumps(data), content_type='application/json')
    
class ListTask(LoginRequiredMixin,ListView):
    model = Tasks
    template_name = 'tasks.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ListTask, self).get_context_data(*args, **kwargs)
        context['tasks'] = Tasks.objects.filter(assigned_user = self.request.user)
        # context['member_project'] =
        return context


class DetailTask(LoginRequiredMixin,DetailView):
    model = Tasks
    template_name = 'taskDetail.html'
    
def GetTask(request):
    if request.is_ajax() and request.method == 'POST':
        task_pk = request.POST.get('task_pk', None)
        obj_task = get_object_or_404(Tasks, pk=int(task_pk))
        data = {
            'name': obj_task.name,
            'description': obj_task.discription,
            'user': obj_task.assigned_user.pk,
            'task_pk': task_pk,
           
    
        }
        return HttpResponse(json.dumps(data), content_type='application/json')

def DeleteTask(request):
    if request.is_ajax() and request.method == 'POST':
        data = {}
        task_pk = request.POST.get('task_pk', None)
        print('task_pk',task_pk)
        Tasks.objects.filter(pk=int(task_pk)).delete()
        data['changes'] = 1
        return HttpResponse(json.dumps(data), content_type='application/json')
        