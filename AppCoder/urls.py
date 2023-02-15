from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('agregar_profes/', agregar_profe, name="agregarprofe"),
    path('ver_estudiantes/', estudiantes, name="Estudiantes"),
    path('ver_profes/', profesores, name="Profesores"),
    path('ver_entregables/', entregables, name="Entregables"),
    path('ver_cursos/', cursos, name="Cursos"),
    path('crear_estudiante/', crear_estudiantes, name="Crear Estudiantes"),
    path('crear_cursos/', crear_cursos, name="Crear Cursos"),
    path('buscar_comision/', busquedaComision, name="Buscar Comision"),
    path('resultados/', resultados, name="Resultadosbusqueda"),
    path('crear_entregables/', crear_entregables, name="CrearEntregables"),
    path('buscar_entregable/', busquedaEntregable, name="BusquedaEntregable"),
    path('resultados2/', resultados2, name="Resultadosbusqueda2"),
    path('buscar_estudiante/', busquedaEstudiante, name="BusquedaEstudiante"),
    path('resultados3/', resultados3, name="Resultadosbusqueda3"),
    path('buscar_profesor/', busquedaProfesor, name="BusquedaProfesor"),
    path('resultados4/', resultados4, name="Resultadosbusqueda4"),
]