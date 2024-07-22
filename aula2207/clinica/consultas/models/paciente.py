from django.core.validators import MinLengthValidator

from consultas.models.base import *
from consultas.models.tipo_alergia import TipoAlergia


class Paciente(BaseModel):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(10)],
                            verbose_name='Nome', help_text="Digite o nome do paciente")
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)],
                           unique=True, verbose_name="CPF", help_text="Digite o CPF")
    endereco = models.CharField(max_length=100, validators=[MinLengthValidator(20)],
                                verbose_name="Endereço", help_text="Digite o endereço completo")
    cidade = models.CharField(max_length=50, validators=[MinLengthValidator(3)],
                              verbose_name="Cidade", help_text="Digite a cidade")
    tipo_alergia = models.CharField(max_length=50, choices=TipoAlergia,
                                    verbose_name="Tipo de Alergia",
                                    help_text="Selecione o tipo  de alergia")
    alergias = models.CharField(max_length=100, validators=[MinLengthValidator(5)],
                                null=True, blank=True, verbose_name="Alergias",
                                help_text="Digite todas as alergias")
    telefone = models.CharField(max_length=20, validators=[MinLengthValidator(10)],
                                verbose_name="Tel", help_text="Digite o telefone com DDD")
    telefone_emergencia = models.CharField(max_length=20, validators=[MinLengthValidator(10)],
                                           verbose_name="Telefone de Emergência",
                                           help_text="Digite o telefone para Emergências com DDD")
    nome_contato = models.CharField(max_length=100, validators=[MinLengthValidator(10)],
                                    verbose_name="Nome para Contato",
                                    help_text="Digite o nome do contato")
    parentesco = models.CharField(max_length=20, validators=[MinLengthValidator(3)],
                                  verbose_name="Parentesco",
                                  help_text="Digite o parentesco do contato")

    def __str__(self):
        return f'{self.cpf} - {self.nome}'

    def paciente_por_cpf(c: str):
        if isinstance(c, str):
            if len(c) == 11:
                return Paciente.objects.get(cpf=c)
            else:
                return ValueError("O CPF informado deve conter 11 digitos")
        else:
            raise TypeError("O CPF informado deve ser do tipo str")

    def pacientes_por_alergia(t: TipoAlergia):
        if isinstance(t, TipoAlergia):
            return list(Paciente.objects.filter(tipo_alergia=t))
        else:
            return TypeError("Deve ser informado um tipo de alergia válido")
