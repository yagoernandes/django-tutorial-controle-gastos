from django.shortcuts import render, redirect
# from django.http import HttpResponse
from datetime import datetime
from .models import Transacao
from .form import TransacaoForm

def home(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, "contas/home.html", data)

def listagem(request):
    data = {}
    data['now'] = datetime.now()
    data['transacoes'] = ['Transacao 1', 'Transacao 2', 'Transacao 3']
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, "contas/listagem.html", data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
      form.save()
      # return home(request)
      return redirect("home")

    return render(request, "contas/nova_transacao.html", { "form": form })

def modificar_transacao(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
      form.save()
      # return home(request)
      return redirect("home")
    data['form'] = form
    data['transacao'] = transacao

    return render(request, "contas/nova_transacao.html", data)

def apagar_transacao(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect("home")
