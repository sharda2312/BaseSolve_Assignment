from django.shortcuts import render

def dna_views(request):
    return render(request, "reverse/index.html")

