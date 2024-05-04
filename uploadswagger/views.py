from django.shortcuts import render, redirect
from .forms import SwaggerFileForm
import os
from django.conf import settings
import subprocess
import json
import time
from django.http import JsonResponse
from .utilities import parseChecker

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
                        "../../restlerBin/restler/Restler.dll test --grammar_file "
                        "Compile/grammar.py --dictionary_file "
                        "Compile/dict.json --settings "
                        "Compile/engine_settings.json --no_ssl")
    os.system(f'{restler_dll_path}')
    json_files = []
    for folder_name in os.listdir("Test/RestlerResults/"):
        print('inside')
        if folder_name.startswith("experiment"):
            # To generate bug_buckets folder, the application has to be running in
            # the backround. We have used pet_store swagger which is uploaded in report
            # We have to run that hava application locally and then run the RESTler Test
            # Otherwise this would give error.
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
    os.chdir('uploadswagger/swagger_files/')
    restler_dll_path = ("dotnet "
                        "../../restlerBin/restler/Restler.dll fuzzlean --grammar_file "
                        "Compile/grammar.py --dictionary_file "
                        "Compile/dict.json --settings "
                        "Compile/engine_settings.json --no_ssl")
    os.system(f'{restler_dll_path}')
    json_files = []
    for folder_name in os.listdir("FuzzLean/RestlerResults/"):
        print('inside')
        if folder_name.startswith("experiment"):
            # To generate bug_buckets folder, the application has to be running in
            # the backround. We have used pet_store swagger which is uploaded in report
            # We have to run that hava application locally and then run the RESTler Fuzzlean
            # Otherwise this would give error.
            os.chdir("FuzzLean/RestlerResults/" + folder_name + "/bug_buckets")
            for file in os.listdir("."):
                if (file.endswith('.json') and not file.lower().startswith("bug")):
                    with open(file, 'r') as f:
                        json_data = json.load(f)
                        print(json_data)
                        json_files.append(json_data)
    os.chdir('../../../')
    return JsonResponse(json_files, safe=False)

def runFuzz(request):
    os.chdir('uploadswagger/swagger_files/')
    restler_dll_path = ("dotnet "
                        "../../restlerBin/restler/Restler.dll fuzz --grammar_file "
                        "Compile/grammar.py --dictionary_file "
                        "Compile/dict.json --settings "
                        "Compile/engine_settings.json --no_ssl")
    os.system(f'{restler_dll_path}')
    json_files = []
    for folder_name in os.listdir("Fuzz/RestlerResults/"):
        print('inside')
        if folder_name.startswith("experiment"):
            # To generate bug_buckets folder, the application has to be running in
            # the backround. We have used pet_store swagger which is uploaded in report
            # We have to run that hava application locally and then run the RESTler Fuzz
            # Otherwise this would give error.
            os.chdir("Fuzz/RestlerResults/" + folder_name + "/bug_buckets")
            for file in os.listdir("."):
                if (file.endswith('.json') and not file.lower().startswith("bug")):
                    with open(file, 'r') as f:
                        json_data = json.load(f)
                        print(json_data)
                        json_files.append(json_data)
    os.chdir('../../../')
    return JsonResponse(json_files, safe=False)
def runMinerFuzz(request):
    os.chdir('MINER/restler_bin_atten/')

    #we can comment it out because fuzz command will take 12-13 hours to run, So
    #we have put the Fuzz folder that was generated and tested the results inside the MINER folder
    restler_dll_path = ("dotnet "
                        "restler/Restler.dll test --grammar_file "
                        "Compile/grammar.py --dictionary_file "
                        "Compile/dict.json --settings "
                        "Compile/engine_settings.json --no_ssl")
    os.system(f'{restler_dll_path}')
    log_data = []
    for folder_name in os.listdir("Fuzz/RestlerResults/"):
        print('inside')
        if folder_name.startswith("experiment"):
            os.chdir("Fuzz/RestlerResults/"+folder_name+"/bug_buckets")
            for file in os.listdir("."):
                if not file.startswith("bug"):
                    file_object = parseChecker(file)
                    log_data.extend(file_object)
    print(log_data)
    return JsonResponse({'logs': log_data})

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
        restler_dll_path = "dotnet ../../restlerBin/restler/Restler.dll compile --api_spec "
        command_line_path = restler_dll_path + uploaded_swagger_file.name
        os.system(f'{command_line_path}')
        os.chdir('../../')
        return render(request, 'uploadswagger/upload.html', {'message': 'File uploaded and Compiled successfully'})
    return render(request, 'uploadswagger/upload.html')

def uploadMiner(request):
    if request.method == 'POST':
        uploaded_swagger_file = request.FILES['swagger_file']
        upload_dir = 'MINER/restler_bin_atten/'
        download_path = os.path.join(upload_dir, uploaded_swagger_file.name)
        with open(download_path, 'wb+') as newfile:
            for chunk in uploaded_swagger_file.chunks():
                newfile.write(chunk)
        print(newfile)
        os.chdir('MINER/restler_bin_atten/')
        restler_dll_path = "dotnet restler/Restler.dll compile --api_spec "
        command_line_path = restler_dll_path + uploaded_swagger_file.name
        os.system(f'{command_line_path}')
        os.chdir('../../')
        return render(request, 'uploadswaggerminer/uploadminer.html', {'message': 'File uploaded and Compiled successfully'})
    return render(request, 'uploadswaggerminer/uploadminer.html')

#     if request.method == 'POST':
#         form = SwaggerFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('results')
#     else:
#         form = SwaggerFileForm()
#     return render(request, 'uploadswagger/upload.html', {'form': form})
