from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from .serializers import PostSerializer

# Create your views here.

"""def home(request):
	context={'posts':Post.objects.all()}
	return render(request,'blog/home.html',context)"""

#Lists the posts in the order of date posted (new to old)
class PostListView(ListView):
	model=Post
	template_name='blog/home.html'
	context_object_name='posts'
	ordering=['-date_posted']
	paginate_by=5

#Tried using REST API for this project lol
"""class PostList(APIView):

	def get(self,request):
		posts=Post.objects.all()
		serializer=PostSerializer(posts,many=True)
		return Response(serializer.data)
"""

#Lists the posts by that specific user
class UserPostListView(ListView):
	model=Post
	template_name='blog/user_posts.html'
	context_object_name='posts'
	ordering=['-date_posted']
	paginate_by=5

	#Function to get the posts from that user (new to old)
	def get_queryset(self):
		user=get_object_or_404(User,username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

#View to display each post 
class PostDetailView(DetailView):
	model=Post

#Create a new post. Requires the user to be logged into his/her account
class PostCreateView(LoginRequiredMixin,CreateView):
	model=Post
	fields=['title','content']

	#Checks validity of the post
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

#Lets the user update their post. Requires user to be logged in
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model=Post
	fields=['title','content']

	#Checks validity of the update form 
	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

	#Checks if the post is being updated by the user who created it	
	def test_func(self):
		
		post=self.get_object()
		
		if self.request.user==post.author:
			return True
		return False

#Lets the user delete their post. Requires the user to be logged in
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post
	success_url='/'

	#Checks if the post is being deleted by the user who created it	
	def test_func(self):
		
		post=self.get_object()
		
		if self.request.user==post.author:
			return True
		return False

#About view (Nothing to see here xD)
def about(request):
	return render(request,'blog/about.html')