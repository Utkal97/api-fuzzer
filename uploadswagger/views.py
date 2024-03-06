from django.shortcuts import render, redirect
from .forms import SwaggerFileForm
import os
from django.conf import settings
import subprocess
import json
import time
from django.http import JsonResponse

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


def runTest(request):
    os.chdir('uploadswagger/swagger_files/')
    restler_dll_path = ("dotnet "
                        "C:/Users/NaraVishnuSai/Desktop/Restler/restler-fuzzer/restler_bin/"
                        "restler/Restler.dll test --grammar_file "
                        "Compile/grammar.py --dictionary_file "
                        "Compile/dict.json --settings "
                        "Compile/engine_settings.json --no_ssl")
    os.system(f'{restler_dll_path}')
    json_files = []
    for folder_name in os.listdir("Test/RestlerResults/"):
        print('inside')
        if folder_name.startswith("experiment"):
            os.chdir("Test/RestlerResults/"+folder_name+"/bug_buckets")
            for file in os.listdir("."):
                if(file.endswith('.json') and not file.lower().startswith("bug")):
                    with open(file, 'r') as f:
                        json_data = json.load(f)
                        print(json_data)
                        json_files.append(json_data)
    os.chdir('../../../')
    return JsonResponse(json_files, safe=False)

def runFuzzLean(request):
    test_folder_path = "uploadswagger/swagger_files/FuzzLean"
    json_files = []

    for file in os.listdir(test_folder_path):
        if(file.endsWith('.json')):
            file_path = os.path(test_folder_path, file)
            with open(file_path, 'r') as f:
                json_data = json.load(f)
            json_files.append(json_data)
    return render(request, 'upload.html', {'json_data': json_data})

def runFuzz(request):
    test_folder_path = "uploadswagger/swagger_files/Fuzz"
    json_files = []

    for file in os.listdir(test_folder_path):
        if(file.endsWith('.json')):
            file_path = os.path(test_folder_path, file)
            with open(file_path, 'r') as f:
                json_data = json.load(f)
            json_files.append(json_data)
    return render(request, 'upload.html', {'json_data': json_data})

def upload(request):
    if request.method == 'POST':
        uploaded_swagger_file = request.FILES['swagger_file']
        upload_dir = 'uploadswagger/swagger_files'
        os.makedirs(upload_dir, exist_ok=True)
        download_path = os.path.join(upload_dir, uploaded_swagger_file.name)
        with open(download_path, 'wb+') as newfile:
            for chunk in uploaded_swagger_file.chunks():
                newfile.write(chunk)
        print(newfile)
        os.chdir('uploadswagger/swagger_files/')
        restler_dll_path = "dotnet C:/Users/NaraVishnuSai/Desktop/Restler/restler-fuzzer/restler_bin/restler/Restler.dll compile --api_spec "
        command_line_path = restler_dll_path + uploaded_swagger_file.name
        os.system(f'{command_line_path}')
        os.chdir('../../')
        return render(request, 'uploadswagger/upload.html', {'message': 'File uploaded and Compiled successfully'})
    return render(request, 'uploadswagger/upload.html')

#     if request.method == 'POST':
#         form = SwaggerFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('results')
#     else:
#         form = SwaggerFileForm()
#     return render(request, 'uploadswagger/upload.html', {'form': form})