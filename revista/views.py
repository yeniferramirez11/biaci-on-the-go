from django.template.response import TemplateResponse

from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from revista.models import Revista

from .forms import ConsultaRevistaForm

from consulta.models import Consulta

def buscador(request):

    if request.method == 'POST':

        form = ConsultaRevistaForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ConsultaRevistaForm()

    return render(request, 'buscar_revista.html', {'form': form})


class RevistaVista(View):

    def post(self, request, *args, **kwargs):

        palabra = request.POST['titulo']

        biblioteca = request.POST['biblioteca']
        por = request.POST['buscar_por']

        if por == '0' and biblioteca == '':
            consulta = Revista.objects.filter(titulo__icontains=palabra)

        if por == '1' and biblioteca == '':
            consulta = Revista.objects.filter(serie__icontains=palabra)

        if por == '2' and biblioteca == '':
            consulta = Revista.objects.filter(cota__icontains=palabra)

        if por == '0' and biblioteca != '':
            consulta = Revista.objects.filter(titulo__icontains=palabra, biblioteca=biblioteca)

        if por == '1' and biblioteca != '':
            consulta = Revista.objects.filter(serie__icontains=palabra, biblioteca=biblioteca)

        if por == '3' and biblioteca != '':
            consulta = Revista.objects.filter(cota__icontains=palabra, biblioteca=biblioteca)

        return TemplateResponse(request, 'revista.html', {'consulta': consulta, 'palabra':palabra})


class EjemplaresVista(View):

    def get(self, request, pk, **kwargs):

        try:
            revista = Revista.objects.get(pk=pk)
        except Revista.DoesNotExist:
            raise Http404("La Revista no existe")

        # book_id=get_object_or_404(Book, pk=pk)
        # Falta agregarle al objeto el titulo y el autor
        busqueda = Consulta(username=request.user,tipo_material="Libro")
        busqueda.save()
        return render(
            request,
            'ejemplar_revista.html',
            context={'ejemplar': revista, }
        )