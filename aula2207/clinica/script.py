from django.contrib.auth import get_user_model
from datetime import time, date

from consultas.models import Paciente, TipoAlergia


User = get_user_model()
User.objects.create_superuser('admin', 'ifrs@restinga.ifrs.edu.br', 'admin')

paciente = Paciente(nome="Ricardo Luis dos Santos",
                    cpf="12345678911",
                    endereco="Rua do IFRS Campus Restinga, 80",
                    cidade="Porto Alegre",
                    tipo_alergia=TipoAlergia.FOOD,
                    alergias="Azeitonas",
                    telefone="51 99999-9999",
                    telefone_emergencia="51 99999-9999",
                    nome_contato="Rodrigo Santos",
                    parentesco="Irmão")

paciente.save()

print(Paciente.paciente_por_cpf("12345678911"))

pacientes = Paciente.pacientes_por_alergia(TipoAlergia.FOOD)
print(pacientes)

for p in pacientes:
    print(p)