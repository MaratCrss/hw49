from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from webapp.models import TrackerType, Tracker, TrackerStatus



class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        kwargs['tasks'] = Tracker.objects.all()
        return super().get_context_data(**kwargs)


class CreateView(View):
    def get(self, request, *args, **kwargs):
        context = {
           'statuses': TrackerStatus.objects.all(),
           'types': TrackerType.objects.all(),
        }
        return render(request, 'create.html', context)
    def post(self, request, *args, **kwargs):

        errors = {}
        type = request.POST.get('type')
        summary = request.POST.get('summary')
        status = request.POST.get('status')
        description = request.POST.get('description')
        if not summary:
            errors['summary'] = 'Ne mojet byt pustym'
        elif len('summary') > 140:
            errors['summary'] = 'Ne dlinnee 140 simvolov'
        elif len(description) > 3000:
            errors['description'] = 'Ne dlinnee 3000 simvolov'
        new_task = Tracker.objects.create(summary=summary, status_id=status, description=description, type_id=type)
        return redirect('task_view', task_pk=new_task.pk)


class TrackerView(TemplateView):
    template_name = 'task_view.html'
    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Tracker, pk=kwargs['task_pk'])
        return super().get_context_data(**kwargs)

