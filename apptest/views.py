from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from django.conf import settings
import base64
import os


@csrf_exempt 
def upload(request):	
    
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
		
        media_root = settings.MEDIA_ROOT
        upload_filename = os.path.join(media_root,filename)
        with open(upload_filename, "rb") as image_file:
            encoded_string = base64.encodebytes(image_file.read())
		
        print (encoded_string)
        return JsonResponse({'status': 'upload', 
		    'file': uploaded_file_url, 
			'data': encoded_string.decode('ascii')})
		      
    return JsonResponse({'upload':'error'})

	
	
def post_list(request, numero=0):
    posts = Post.objects.filter(title__contains='title')
    return render(request, 'apptest/post_list.html', {'posts': posts})

	
def test_page(request,dato=0):
    return render(request, 'apptest/test_page.html',  {'dato': dato})
	

def test_json(request):
	return JsonResponse({'foo':'bar'})

def no_autorizado(request):
	return JsonResponse({'error':'no autorizado'})

@login_required(login_url='/test/noautorizado/')
def test_autenticar(request):
	return JsonResponse({'foo':'autenticado'})

def autenticar(request):
    username = 'marcos'
    password = 'hall9000'
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return JsonResponse({'foo':'autenticado'})
    else:
        # Return an 'invalid login' error message.
        return JsonResponse({'foo':'no autenticado'})