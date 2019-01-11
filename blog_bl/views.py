from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from . import forms


# Create your views here.
def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog_bl/post_list.html', {'posts': posts})

def post_create(request):
	form=forms.CreatePost()
	if request.method=='POST':
		# form=forms.CreatePost(request.POST, request.FILES)
		form=forms.CreatePost(request.POST)
		if form.is_valid():
			return redirect ('post_list')
		else:
			form=forms.CreatePost()
	return render(request, 'blog_bl/post_create.html', {'form':form})	