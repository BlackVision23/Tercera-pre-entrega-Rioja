from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def agregar_profe(request):

    if request.method == 'POST':

        miFormulario = formularioProfes(request.POST)

        if miFormulario.is_valid():

            infoDic = miFormulario.cleaned_data

            profe1 = Profesor(nombre=infoDic['nombre'], apellido = infoDic['apellido'], email = infoDic['email'], profesion = infoDic['profesion'])

            profe1.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = formularioProfes()

    return render(request, "AppCoder/crearProfesores.html", {"formulario3":miFormulario})

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

        return render(request, "AppCoder/resultados.html", {"cursos":cursos, "comision":comision})

    else:

        respuesta = "no enviaste datos."
    
    return HttpResponse(respuesta)

def crear_entregables(request):

    if request.method == 'POST':

        miFormulario = formularioEntregables(request.POST)

        if miFormulario.is_valid():

            infoDic = miFormulario.cleaned_data

            entregable1 = Entregable(nombre=infoDic['nombre'], fechaDeEntrega = infoDic['fechaDeEntrega'], entregado = infoDic['entregado'])

            entregable1.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = formularioEntregables()

    return render(request, "AppCoder/crearEntregables.html", {"formulario2":miFormulario})

def busquedaEntregable(request):

    return render(request, "AppCoder/buscarEntregable.html")

def busquedaEstudiante(request):

    return render(request, "AppCoder/buscarEstudiante.html")

def resultados2(request):

    if request.GET["fechaDeEntrega"]:

        fechaDeEntrega = request.GET["fechaDeEntrega"]
        entregables = Entregable.objects.filter(fechaDeEntrega=fechaDeEntrega)

        return render(request, "AppCoder/resultados2.html", {"entregables":entregables, "fechaDeEntrega":fechaDeEntrega})

    else:

        respuesta = "no enviaste datos."
    
    return HttpResponse(respuesta)

def resultados3(request):

    if request.GET["email"]:

        email = request.GET["email"]
        estudiantes = Estudiante.objects.filter(email=email)
        
        return render(request, "AppCoder/resultados3.html", {"estudiantes":estudiantes, "email":email})

    else:

        respuesta = "no enviaste datos."
    
    return HttpResponse(respuesta)

def busquedaProfesor(request):

    return render(request, "AppCoder/buscarProfesor.html")

def resultados4(request):

    if request.GET["email"]:

        email = request.GET["email"]
        profesores = Profesor.objects.filter(email=email)

        return render(request, "AppCoder/resultados4.html", {"profesores":profesores, "email":email})

    else:

        respuesta = "no enviaste datos."
    
    return HttpResponse(respuesta)