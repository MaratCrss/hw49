from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import View, TemplateView, RedirectView, FormView
from webapp.models import TrackerType, Tracker, TrackerStatus
from webapp.forms import TrackerForm
from webapp.base_view import FormView as CustomFormView




class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Tracker.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        for task_pk in request.POST.getlist('tasks', []):
            Tracker.objects.get(pk=task_pk).delete()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class CreateView(CustomFormView):
    template_name = 'create.html'
    form_class = TrackerForm

    def get_redirect_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)



class TrackerView(TemplateView):
    template_name = 'task_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Tracker, pk=kwargs['pk'])
        return context


class UpdateTask(FormView):
    template_name = "update.html"
    form_class = TrackerForm

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Tracker, pk=pk)

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Tracker, pk=pk)


class DeleteTask(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Tracker, pk=kwargs['pk'])
        return render(request, 'delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Tracker, pk=kwargs['pk'])
        task.delete()
        return redirect('index')

class MyRedirectView(RedirectView):
    url = 'https://https://www.google.com/'