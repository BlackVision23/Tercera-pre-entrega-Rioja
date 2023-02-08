from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('agregar_profes/', agregar_profe),
    path('ver_estudiantes/', estudiantes, name="Estudiantes"),
    path('ver_profes/', profesores, name="Profesores"),
    path('ver_entregables/', entregables, name="Entregables"),
    path('ver_cursos/', cursos, name="Cursos"),
    path('crear_estudiante/', crear_estudiantes, name="Crear Estudiantes"),
    path('crear_cursos/', crear_cursos, name="Crear Cursos"),
    path('buscar_comision/', busquedaComision, name="Buscar Comision"),
    path('resultados/', resultados, name="Resultados busqueda"),
]