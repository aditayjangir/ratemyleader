from .models import PoliticianDetail
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.forms import modelformset_factory
from django.contrib import messages

# Create your views here.
def home(request):
    print(request.user.id)
    # data_set = request.user.id
    # print("****",data_set)
    # data = {
    #     'data_set':data_set,
    # }
    return render(request, 'webpages/home.html')
def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')

def politiciandetails(request):
    # pk = request.GET.get('pk', None)
    details = get_object_or_404(PoliticianDetail,id=3)
    userss = request.user.get_username()
    is_liked = False
    for like in details.likes:
        print(like)
    if details.likes.values_list(userss, flat=True):
       is_liked = True
    data={
        'total_likes':details.total_likes(),
        'details':details,
        'is_liked':is_liked,
    }
    return render(request,'webpages/politiciandetails.html',data)

# def update_likes(request):
#     if request.method == 'POST':
#         PoliticianDetails = PoliticianDetail.objects.get()
#         PoliticianDetails.button_like =  request.POST['counter']
#         PoliticianDetails.save()
#         message = 'update successful'
#     return HttpResponse(message)

# def update_dislikes(request):
    # if request.method == 'POST':
    #     PoliticianDetails = PoliticianDetail.objects.get()
    #     PoliticianDetails.button_dislike =  request.POST['counter']
    #     PoliticianDetails.save()
    #     message = 'update successful'
    # return HttpResponse(message)

def like_post(request):
    
    post = get_object_or_404(PoliticianDetail, id=request.POST.get('id'))    
    
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
        
    else:
        post.likes.add(request.user)
        is_liked = True
        
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('webpages/like_section.html', context, request=request)
        return JsonResponse({'form': html})