from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'  # ключ по которому будем передавть запись внутрь шаблона


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)  # данные полученные от user из формы
        if form.is_valid():
            form.save()
            return redirect('news_home')  # переадрессация
        else:
            error = 'Форма была  неверной'

    forms = ArticlesForm()
    date = {
        'form': forms,
        'error': error
    }
    return render(request, 'news/create.html', date)
