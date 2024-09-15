from django.http import HttpResponse
from django.template import Template, Context

def principal (request):
    # abrir documento principal
    paginaPrincipal = open("C:\\Users\\Felipe\\Desktop\\eva_01_backend\\eva_1\\eva_1\\templates\\index.html")
    # Cargar documento en un template
    template = Template(paginaPrincipal.read())
    # cerrar documetno
    paginaPrincipal.close()
    # crear contexto
    contexto = Context()
    # Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)
