from django.db import models
from math import floor, ceil

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereco = models.CharField(max_length=100, blank=True, null=True, verbose_name='Endereço')
    complemento = models.CharField(max_length=50, blank=True, null=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=50, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    telefone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Telefone')
    email = models.EmailField(verbose_name='Email')
    foto = models.ImageField(upload_to='cliente_foto', blank=True, null=True, verbose_name=' ')

    def __str__(self):
        return self.nome


class Marca(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome Marca')
    url = models.URLField(verbose_name='Site', blank=True, null=True)
    logo = models.ImageField(upload_to='marca_logo', blank=True, null=True, verbose_name=' ')

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    placa = models.CharField(max_length=8, verbose_name='Placa')
    modelo = models.CharField(max_length=30, blank=True, null=True, verbose_name='Modelo')
    cor = models.CharField(max_length=30, blank=True, null=True, verbose_name='Cor')
    ano = models.IntegerField(default=2023, blank=True, null=True, verbose_name='Ano')
    foto = models.ImageField(upload_to='veiculo_foto', blank=True, null=True, verbose_name=' ')
    marca_id = models.ForeignKey(Marca, on_delete=models.DO_NOTHING, verbose_name='Marca')
    cliente_id = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, verbose_name='Cliente')

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

    class Meta:
        verbose_name_plural = 'Veículos'

class Tabela(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Preço')

    def __str__(self):
        return f'{self.descricao} - {self.preco}'

    class Meta:
        verbose_name_plural = 'Tabelas'


class Mensalista(models.Model):
    idVeiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veiculo')
    idTabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name='Preço')
    observacoes = models.TextField(blank=True, null=True, verbose_name='OBS:')

    class Meta:
        verbose_name_plural = 'Mensalistas'

    def __str__(self):
        return self.idVeiculo

class Rotativo(models.Model):
    idVeiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, verbose_name='Veiculo')
    idTabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, verbose_name='Tabela')
    horaEntrada = models.DateTimeField(auto_now=False, verbose_name='Hora entrada')
    horaSaida = models.DateTimeField(auto_now=False, blank=True, null=True, verbose_name='Hora saida')
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='Total')
    pago = models.BooleanField(default=False, verbose_name='Pago')
    observacoes = models.TextField(blank=True, null=True, verbose_name='OBS:')

    class Meta:
        verbose_name_plural = 'Rotativos'

    def __str__(self):
        return f'{self.idVeiculo} - {self.idTabela}'

    def calculaTotal(self):
        if self.horaSaida:
            hora = (self.horaSaida - self.horaEntrada).total_seconds()/3600
            obj = Tabela.objects.get(id=self.idTabela.pk)
            if hora <= 0.5:
                self.total = obj.preco / 2
            else:
                self.total = ceil(hora * float(obj.preco))
            return self.total
        else:
            return 0.0
