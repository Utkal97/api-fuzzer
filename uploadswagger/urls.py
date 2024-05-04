from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload, name="upload"),
    path("miner/", views.uploadMiner, name="uploadMiner"),
    path("runTest/", views.runTest, name="runTest"),
    path("runFuzzLean/", views.runFuzzLean, name="runFuzzLean"),
    path("runFuzz/", views.runFuzz, name="runFuzz"),
    path("runMinerFuzz/", views.runMinerFuzz, name="runMinerFuzz"),
    path("results", views.results, name="results"),
]

