from django.shortcuts import render, redirect
from .forms import SwaggerFileForm
import os
from django.conf import settings

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
    test_folder_path = "uploadswagger/swagger_files/Test"
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
        download_path = os.path.join('uploadswagger/swagger_files', uploaded_swagger_file.name)
        with open(download_path, 'wb+') as newfile:
            for chunk in uploaded_swagger_file.chunks():
                newfile.write(chunk)
        print(newfile)
#         restler_dll_path = "/Users/laxmanmadipadige/Documents/restler-fuzzer/restler_bin/restler/Restler.dll"
#         command_line_path = f"compile --api_spec {download_path}"
#         subprocess.run(["dotnet" , restler_dll_path, command_line_path])
        return render(request, 'uploadswagger/upload.html')
    return render(request, 'uploadswagger/upload.html')

#     if request.method == 'POST':
#         form = SwaggerFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('results')
#     else:
#         form = SwaggerFileForm()
#     return render(request, 'uploadswagger/upload.html', {'form': form})