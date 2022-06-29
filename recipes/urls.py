from django.urls import path

from recipes.views import teste_teste

# def teste_teste(request):
#    return HttpResponse('Vamos ver!')


urlpatterns = [
    path('teste/', teste_teste)
]
