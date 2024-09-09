from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Blazer',
        'price': '2000000',
        'description': 'Pink'
    }

    return render(request, "main.html", context)