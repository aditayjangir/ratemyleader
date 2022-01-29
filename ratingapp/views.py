from .models import PoliticianDetail
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')
def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')

def politiciandetails(request):
    # pk = request.GET.get('pk', None)
    details = PoliticianDetail.objects.all
    userss = request.user.get_username()
    data={
        # 'total_likes':PoliticianDetail.total_likes(),
        'details':details,
        'userss':userss,
    }
    return render(request,'webpages/politiciandetails.html',data)

def like_post(request):
    userss = request.user.get_username()
    post = get_object_or_404(PoliticianDetail, id=request.POST.get('id'))    
    first = PoliticianDetail(likes={'likes':[]})
    first.save()
    result = PoliticianDetail.objects.all()
    like_list = result[id].likes
    like_list['likes'].append(userss)
    is_liked = True
    # if post.likes.filter().exists():
    #     post.likes.remove(request.user)
    #     is_liked = False
        
    # else:
    #     post.likes.add(request.user)
    #     is_liked = True
        
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('webpages/like_section.html', context, request=request)
        return JsonResponse({'form': html})