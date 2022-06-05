from django.http import HttpResponse, HttpResponseRedirect
from multiprocessing import context
from re import template
from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView, TemplateView


class NewsHome(TemplateView):
    template_name = 'news/news_home.html'

    def get_context_data(self, **kwargs):
        context = super(NewsHome, self).get_context_data(self, **kwargs)
        context['posts'] = Post.objects.order_by('title')
        return context


class NewsDetailView(DeleteView):
    model = Post
    template_name = 'news/details_view.html'        
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Post
    template_name = 'news/create.html'
    form_class = PostForm


class NewsDeleteView(DeleteView):
    model = Post
    success_url = '/news'
    template_name = 'news/news_delete.html'


class Create(View):
    form_class = PostForm
    initial = {'key': 'value'}
    template_name = 'news/create.html'
     