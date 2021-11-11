from django.shortcuts import render
from mod.models import Empleado


def index(request):
     return render(request, "mod/Modificar.html")

def result(request):
    numeroEmpleado = request.POST['txtEmpno']
    nuevoSalario = request.POST['txtNewSalario']
    emple = Empleado()
    cursor=emple.devolverdato(numeroEmpleado, nuevoSalario)
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "mod/Resultado.html", contexto)
