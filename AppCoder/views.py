from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def agregar_profe(request):

    profe1 = Profesor(nombre = "gaby", apellido = "rioja", email = "gabr@gmail.com", profesion = "genio")
    profe1.save()
    return HttpResponse (f"Hemos creado al profesor {profe1.nombre} a la base de datos.")

def estudiantes(request):

    return render(request, "AppCoder/verEstudiantes.html")

def profesores(request):

    return render(request, "AppCoder/verProfesores.html")

def entregables(request):

    return render(request, "AppCoder/verEntregables.html")

def cursos(request):

    return render(request, "AppCoder/verCursos.html")

def crear_estudiantes(request):

    if request.method == 'POST':

        estudiante1 = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])

        estudiante1.save()

        return render(request, "AppCoder/inicio.html")

    return render(request, "AppCoder/crearEstudiantes.html")

def crear_cursos(request):

    if request.method == 'POST':

        miFormulario = formularioCurso(request.POST)

        if miFormulario.is_valid():

            infoDic = miFormulario.cleaned_data

            curso1 = Curso(nombre=infoDic['nombre'], comision= infoDic['comision'])

            curso1.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = formularioCurso()

    return render(request, "AppCoder/crearCursos.html", {"formulario1":miFormulario})

def busquedaComision(request):

    return render(request, "AppCoder/buscarComision.html")

def resultados(request):

    if request.GET["comision"]:

        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision=comision)

        return render(request, "AppCoder\templates\AppCoder\resultados.html", {"cursos":cursos, "comision":comision})

    else:

        respuesta = "no enviaste datos."
    
    return HttpResponse(respuesta)