from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .models import Photo
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import BlogPost

def blog(request):
    
    blogs = Blog.objects

    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    print(page)
    print(posts)



    return render(request, 'blog.html' ,{'blogs':blogs, 'posts':posts})

def blogpost(request):
    #입력된 내용 처리
    
    #빈페이지 띄워주기
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.date = timezone.now()
            post.save()
            return redirect('blog')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def detail(request, blog_id):

    blog = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):

    blog = Blog()
    blog.title = request.GET['title']
    blog.content = request.GET['content']
    blog.date = timezone.datetime.now()
    blog.save()


    return redirect('/blog/'+str(blog.id))

def photo(request):
    photos = Photo.objects
    return render(request, 'photo.html', {'photos' : photos})
