from django.shortcuts import render, redirect
from core.forms import FormularioCliente, FormularioVeiculo, FormularioTabela, FormularioMarca, FormularioMensalista, FormularioRotativo
from core.models import Cliente, Veiculo, Tabela, Marca, Mensalista, Rotativo
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'

def home(request):
    return render(request, 'core/index.html')

@login_required
def cadastroCliente(request):
    if request.user.is_staff:
        form = FormularioCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('url_principal')
        contexto = {'form': form, 'txt_title': 'Cadastro Cliente', 'txt_header': 'Cadastro Cliente'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroVeiculo(request):
    if request.user.is_staff:
        form = FormularioVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso!')
            return redirect('url_listagem_veiculos')
        contexto = {'form': form, 'txt_title': 'Cadastro Veículo', 'txt_header': 'Cadastro Veículo'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroTabela(request):
    if request.user.is_staff:
        form = FormularioTabela(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_tabelas')
        contexto = {'form': form, 'txt_title': 'Cadastro Tabela Precos', 'txt_header': 'CADASTRO PREÇOS'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required
def cadastroMarca(request):
    if request.user.is_staff:
        form = FormularioMarca(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_marcas')
        contexto = {'form': form, 'txt_title': 'Cadastro Marcas', 'txt_header': 'CADASTRO MARCA'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required
def cadastroMensalista(request):
    if request.user.is_staff:
        form = FormularioMensalista(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_mensalistas')
        contexto = {'form': form, 'txt_title': 'Cadastro Mensalista', 'txt_header': 'CADASTRO MENSALISTA'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')

@login_required
def cadastroRotativo(request):
    if request.user.is_staff:
        form = FormularioRotativo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_rotativos')
        contexto = {'form': form, 'txt_title': 'Cadastro Rotativo', 'txt_header': 'CADASTRO ROTATIVO'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemVeiculos(request):
    if request.user.is_staff:
        dados = Veiculo.objects.all()
        contexto = {'dados': dados, 'txt_input': 'Digite uma placa'}
        return render(request, 'core/listagem_veiculos.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listagemClientes(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Cliente.objects.filter(nome__contains = request.POST['input_pesquisa'])
        else:
            dados = Cliente.objects.all()
        contexto = {'dados': dados, 'txt_input': 'Digite um nome'}
        return render(request, 'core/listagem_clientes.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listagemTabelas(request):
    if request.user.is_staff:
        dados = Tabela.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_tabelas.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemMarcas(request):
    if request.user.is_staff:
        dados = Marca.objects.all()
        contexto = {'dados': dados, }
        return render(request, 'core/listagem_marcas.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listagemMensalistas(request):
    if request.user.is_staff:
        dados = Mensalista.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_mensalistas.html', contexto)
    return render(request, 'aviso.html')

@login_required
def listagemRotativos(request):
    if request.user.is_staff:
        dados = Rotativo.objects.all()
        contexto = {'dados': dados}
        return render(request, 'core/listagem_rotativos.html', contexto)
    return render(request, 'aviso.html')


@login_required
def alteraCliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormularioCliente(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, 'Dados alterados com sucesso!')
                return redirect('url_listagem_clientes')
        contexto = {'form': form, 'txt_titulo': 'EditCliente', 'txt_header': 'ALTERAR CLIENTE'}
        return render(request, 'core/cadastro.html', contexto)

    return render(request, 'core/aviso.html')

@login_required
def alteraVeiculo(request, id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id=id)
        form = FormularioVeiculo(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, 'Dados alterados com sucesso!')
                return redirect('url_listagem_veiculos')
        contexto = {'form': form, 'txt_titulo': 'EditVeiculo', 'txt_header': 'ALTERAR VEICULO'}
        return render(request, 'core/cadastro.html', contexto)

    return render(request, 'core/aviso.html')


@login_required
def alteraTabela(request, id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id=id)
        form = FormularioTabela(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_tabelas')
        contexto = {'form': form, 'txt_titulo': 'EditTabela', 'txt_header': 'ALTERAR TABELA DE PREÇO'}
        return render(request, 'core/cadastro.html', contexto)

    return render(request, 'core/aviso.html')

@login_required
def alteraMarca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id=id)
        form = FormularioMarca(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_marcas')
        contexto = {'form': form, 'txt_titulo': 'EditMarcas', 'txt_header': 'ALTERAR MARCAS'}
        return render(request, 'core/cadastro.html', contexto)

    return render(request, 'core/aviso.html')

def alteraRotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id=id)
        form = FormularioRotativo(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                obj.calculaTotal()
                form.save()
                return redirect('url_listagem_rotativos')
        contexto = {'form': form, 'txt_titulo': 'EditRotativo', 'txt_header': 'ALTERAR ROTATIVO'}
        return render(request, 'core/cadastro.html', contexto)

    return render(request, 'core/aviso.html')

def alteraMensalista():
    pass


def excluiCliente(request, id):
    obj = Cliente.objects.get(id=id)
    contexto = {'txt_info': obj.nome, 'txt_url': '/listagemClientes/'}
    if request.POST:
        obj.delete()
        messages.success(request, 'Cliente deletado com sucesso.')
        contexto.update({'txt_tipo': 'listagemClientes'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def excluiVeiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    contexto = {'txt_info': obj.placa, 'txt_url': '/listagemVeiculos/'}
    if request.POST:
        obj.delete()
        messages.success(request, 'Veículo deletado com sucesso.')
        contexto.update({'txt_tipo': 'listagemVeiculos'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def excluiRotativo(request, id):
    obj = Rotativo.objects.get(id=id)
    contexto = {'txt_info': f'{obj.idVeiculo}, {obj.horaEntrada}', 'txt_url': '/listagemRotativos/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo': 'listagemRotativos'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def excluiMensalista(request, id):
    obj = Mensalista.objects.get(id=id)
    contexto = {'txt_info': f'{obj.idVeiculo}', 'txt_url': '/listagemMensalistas/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo': 'listagemMensalistas'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)

