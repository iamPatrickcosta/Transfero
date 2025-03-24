from django.shortcuts import render

# aqui irão ficar todas as views ( controladores) ref ao sistema
# A função index informa o que vai acontecer  
def index(request):
    return render(
        request,
        'sistema/index.html',
    )

