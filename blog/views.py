from django.shortcuts import render

def blog(request):
    print('blog')

    context = {
        'text': 'Ola blog'
    }

    return render(request, 'blog/index.html', context)

def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Ola exemplo',
        'title': 'Site do Exemplo - ',
    }

    print('exemplo')
    return render(request, 'blog/exemplo.html', context)