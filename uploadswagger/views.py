from django.shortcuts import render, redirect
from .forms import SwaggerFileForm

def results(request):
    context = {}
    if request.method == 'GET':
        context = {
            "swagger_file": "swagger.json",
            "bug_count": 3,
            "bug_details": [
                {
                    "end_point": "/blog/posts",
                    "method": "GET",
                    "failure": "Didn't pass Payload Check"
                },
                {
                    "end-point": "/blog/post",
                    "method": "POST",
                    "failure": "Didn't pass Valid params Check"
                },
                {
                    "end_point": "/blog/users",
                    "method": "GET",
                    "failure": "Didn't pass Memory leak Check"
                },
            ]
        }
    return render( request, "uploadswagger/results.html", context)

def upload(request):
    if request.method == 'POST':
        form = SwaggerFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('results')
    else:
        form = SwaggerFileForm()
    return render(request, 'uploadswagger/upload.html', {'form': form})