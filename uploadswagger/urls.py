from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload, name="upload"),
    path("runTest/", views.runTest, name="runTest"),
    path("runFuzzLean/", views.runFuzzLean, name="runFuzzLean"),
    path("runFuzz/", views.runFuzz, name="runFuzz"),
    path("results", views.results, name="results"),
]

