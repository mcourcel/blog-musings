# Create your views here.
from django.shortcuts import render, get_object_or_404
from blog.models import Post
import markdown

def index(request):
	#get the blog posts that are published
	posts = Post.objects.filter(published=True)
	#Now return the rendered template.
	return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
	#Get the post object.
	post = get_object_or_404(Post, slug=slug)
	#markdown to html
	markdown_post = markdown.markdown(post.content)
	#Now return the rendered template.
	return render(request, 'blog/post.html', {'post': post, 'content': markdown_post})
 