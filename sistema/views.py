from django.shortcuts import render

# aqui irão ficar todas as views ( controladores) ref ao sistema

def index(request):
    return render(
        request,
        'sistema/index.html',
    )

