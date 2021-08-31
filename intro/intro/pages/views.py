from django.shortcuts import render

# Create your views here.
def dinner(request, menu, number):
    context = {
        'menu' : menu,
        'number' : number,
    }

    return render(request, 'dinner.html', context)