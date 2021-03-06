from django.shortcuts import render
from .models import Post#PublishedManager
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
# Create your views here.

#List of pusblished posts
#Function based view 
# def post_list(request):
#     posts=Post.published.all()
#     paginator=Paginator(posts,3)
#     page=request.GET.get('page')
#     try:
#         posts=paginator.page(page)
#     except PageNotAnInteger:
#         posts=paginator.page(1)
#     except EmptyPage:
#         posts=paginator.page(paginator.num_pages)

#     return render(request,'blog/post/list.html',{'page':page,'posts':posts})

class PostListView(ListView):
    queryset=Post.published.all()
    context_object_name='posts'

    paginate_by=3
    template_name='blog/post/list.html'


def post_detail(request,year,month,day,post):
    print('#')
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year ,\
                            publish__month=month,publish__day=day)
    
    print('######')
    print(post)
    return render (request,'blog/post/detail.html',{'post':post})


def post_share(request,post_id):
    print('Share post')
    post=get_object_or_404(Post,id=post_id,status='published')
    sent=False
    if request.method =='POST':
        form=EmailPostForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{} {} recommends your reading {}'.format(cd.name,cd.email,post.title)
            message='{} at {}\n\n comments:{}'.format(post.title,post_url,cd['name',cd['comments']])
            send_mail(subject,message,'tripathiabhishek868@gmail.com',[cd['to']])
            sent=True
    else:
    
        form=EmailPostForm()
       
    return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent})
        
        
        
        
    form=EmailPostForm()
