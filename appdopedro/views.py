from django.shortcuts import render, redirect
from .models import Dias, Estatisticas, Fred

# Create your views here.
def home(request):
  estatisticas = Estatisticas.objects.all()
  dias = Dias.objects.all()
  inf = Fred.objects.all()
  return render(request, "home.html", context={
    "dias" : dias,
    "num" : estatisticas,
    "inf" : inf
  })

def create_dia(request):
  if request.method == "POST":
    Dias.objects.create(
     descricao = request.POST["descricao"],
     ano = request.POST["ano"],
     impacto = request.POST["impacto"]
    )

    return redirect("home")
  options = Dias.impacto.field.choices
  return render(request,"forms.html", context={"type" : "Adicionar", "options": options})

def create_numero(request):
  if request.method == "POST":
    Estatisticas.objects.create(
    categoria = request.POST["categoria"],
    numeros = request.POST["numero"],
    )

    return redirect("home")
  return render(request,"forms2.html", context={"type" : "Adicionar"})

def update_dia(request,id):
  dia = Dias.objects.get(id=id)
  if request.method == "POST":
     dia.descricao = request.POST["descricao"]
     dia.ano = request.POST["ano"]
     dia.impacto = request.POST["impacto"]
     dia.save()
    
     return redirect("home")
  options = Dias.impacto.field.choices
  return render(request,"forms.html", context = {"type": "Atualizar","dia" : dia, "options": options})

def update_numero(request, id):
  numero = Estatisticas.objects.get(id=id)
  if request.method == "POST":
    numero.categotia = request.POST["categoria"]
    numero.numeros = request.POST["numeros"]
    numero.save()

    return redirect("home")
  return render(request,"forms2.html", context={"type": "Atualizar", "numero" : numero})

def delete_dia(request,id):
  dia = Dias.objects.get(id=id)
  if request.method == "POST":
    if request.POST["Sim"]:
      dia.delete()
    
    return redirect("home")
  return render(request,"are_u_sure2.html", context = {"type": "Deletar","dia" : dia})

def delete_numero(request, id):
  numero =Estatisticas.objects.get(id=id)
  if request.method == "POST":
    if request.POST["Sim"]:
       numero.delete()

    return redirect("home")
  return render(request,"are_u_sure.html", context={"type": "Deletar", "numero" : numero})