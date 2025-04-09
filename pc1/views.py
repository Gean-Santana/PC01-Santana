from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    tareas = Tarea.objects.all().order_by('-fecha_creacion')
    return render(request, 'pc1/lista.html', {'tareas': tareas})

def crear_tarea(request):
    form = TareaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_tareas')
    return render(request, 'pc1/formulario.html', {'form': form})

def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    form = TareaForm(request.POST or None, instance=tarea)
    if form.is_valid():
        form.save()
        return redirect('lista_tareas')
    return render(request, 'pc1/formulario.html', {'form': form})

def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    return render(request, 'pc1/confirmar_eliminar.html', {'tarea': tarea})