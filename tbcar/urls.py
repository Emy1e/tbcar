"""tbcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import home, cadastroCliente, cadastroVeiculo, cadastroTabela, cadastroMarca, cadastroRotativo, cadastroMensalista, \
    listagemClientes, listagemVeiculos, listagemTabelas, listagemMarcas, listagemRotativos, listagemMensalistas, \
    Registrar, alteraCliente, alteraVeiculo, alteraTabela, alteraMarca, alteraRotativo, alteraMensalista, \
    excluiCliente, excluiVeiculo, excluiMensalista, excluiRotativo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_principal'),
    path('cadastroCliente/', cadastroCliente, name='url_cadastro_cliente'),
    path('cadastroVeiculo/', cadastroVeiculo, name='url_cadastro_veiculo'),
    path('cadastroTabela/', cadastroTabela, name='url_cadastro_tabela'),
    path('cadastroMarca/', cadastroMarca, name='url_cadastro_marca'),
    path('cadastroMensalista/', cadastroMensalista, name='url_cadastro_mensalista'),
    path('cadastroRotativo/', cadastroRotativo, name='url_cadastro_rotativo'),
    path('listagemClientes/', listagemClientes, name='url_listagem_clientes'),
    path('listagemVeiculos/', listagemVeiculos, name='url_listagem_veiculos'),
    path('listagemTabelas/', listagemTabelas, name='url_listagem_tabelas'),
    path('listagemMarcas/', listagemMarcas, name='url_listagem_marcas'),
    path('listagemMensalistas/', listagemMensalistas, name='url_listagem_mensalistas'),
    path('listagemRotativos/', listagemRotativos, name='url_listagem_rotativos'),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('alteraCliente/<int:id>/', alteraCliente, name='url_altera_cliente'),
    path('alteraVeiculo/<int:id>/', alteraVeiculo, name='url_altera_veiculo'),
    path('alteraTabela/<int:id>/', alteraTabela, name='url_altera_tabela'),
    path('alteraMarca/<int:id>/', alteraMarca, name='url_altera_marca'),
    path('alteraRotativo/<int:id>/', alteraRotativo, name='url_altera_rotativo'),
    path('excluiCliente/<int:id>/', excluiCliente, name='url_exclui_cliente'),
    path('excluiVeiculo/<int:id>/', excluiVeiculo, name='url_exclui_veiculo'),
    path('excluiMensalista/<int:id>/', excluiMensalista, name='url_exclui_mensalista'),
    path('excluirRotativo/<int:id>/', excluiRotativo, name='url_exclui_rotativo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
