from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama' : 'Alya Rasheeda Yuvana',
        'kelas' : 'PBP B',
        'name' : 'Blazer',
        'price': '2000000',
        'description': 'Pink'
    }

    return render(request, "main.html", context)