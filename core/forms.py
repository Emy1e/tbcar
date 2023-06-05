from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from captcha.fields import CaptchaField
from django.forms import ModelForm
from core.models import Cliente, Veiculo, Marca, Tabela, Mensalista, Rotativo


class FormularioCliente(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Cliente
        fields = '__all__'


class FormularioVeiculo(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Veiculo
        fields = '__all__'


class FormularioMarca(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Marca
        fields = '__all__'


class FormularioTabela(ModelForm):

    class Meta:
        model = Tabela
        fields = '__all__'

class FormularioMensalista(ModelForm):

    class Meta:
        model = Mensalista
        fields = '__all__'


class FormularioRotativo(ModelForm):

    class Meta:
        model = Rotativo
        fields = '__all__'

        widgets = {'horaEntrada': DateTimePickerInput(), 'horaSaida': DateTimePickerInput()}
