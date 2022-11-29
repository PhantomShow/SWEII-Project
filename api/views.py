from django.shortcuts import render
from django.db.models import Q
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from . import forms
from . import models
# Create your views here.

# class HomePage(ListView):
#     model = models.CustomUser
#     template_name = 'index.html'
#     context_object_name = 'user_list'

#     # This makes it possible to have both a user_list, posts list, and form in one view
#     def get_context_data(self, **kwargs):
#         context = super(HomePage, self).get_context_data(**kwargs)
#         context.update({
#             'posts': models.Post.objects.all().order_by('-create_date'), # Newest first
#             'form': forms.PostForm,
#         })
#         return context

def home_page(request):
    user_list = models.CustomUser.objects.all()
    posts = models.Post.objects.all().order_by('-create_date')

    if request.method == 'POST':
        if 'post_submit' in request.POST:
            post_form = forms.PostForm(request.POST)
            if post_form.is_valid():
                post_form.instance.author = request.user
                post_form.save()
                post_form = forms.PostForm()
            comment_form = forms.CommentForm()
        elif 'comment_submit' in request.POST:
            comment_form = forms.CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form.instance.author = request.user
                comment_father = models.Post.objects.get(pk= request.POST.get("comment_father", ""))
                comment_form.instance.post = comment_father
                comment_form.save()
                comment_form = forms.CommentForm()
            post_form = forms.PostForm()
    else:
        post_form = forms.PostForm()
        comment_form = forms.CommentForm()
    
    context = {'user_list': user_list, 'posts':posts, 'post_form':post_form, 'comment_form':comment_form}

    return render(request, 'index.html', context)

class UserDetail(DetailView):
    model = models.CustomUser
    template_name = 'user_detail.html'
    context_object_name = 'user_detail'

    # This makes it possible to have both a user_detail and user_posts in one view
    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        context.update({
            'user_posts': models.Post.objects.filter(author=context['user_detail']).order_by('-create_date'), # Newest first
        })
        return context

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UpdateUser(UpdateView):
    model = models.CustomUser
    form_class = forms.UserEditForm
    success_url = reverse_lazy('api:home_page')
    template_name = 'user_update.html'

class DeletePost(DeleteView):
    model = models.Post
    success_url = reverse_lazy('api:home_page')
    # context_object_name = 'post'
    template_name = 'post_delete.html'

def search_results(request):
    if request.method == 'POST':
        target = request.POST['searchQueryInput']
        users = models.CustomUser.objects.filter( Q(username__contains=target) | Q(school__contains=target) )
        return render(request, 'search_results.html', {'target':target, 'users':users})
    
    else:
        return render(request, 'search_results.html', {})