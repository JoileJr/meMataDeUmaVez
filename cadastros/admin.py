from django.contrib import admin

from .models import (
    Endereco,
    Barbearia,
    Administrador,
    Barbeiro,
    Servico,
    Cliente,
    Agendamento,
    Pagamento,
)

admin.site.register(Endereco)
admin.site.register(Barbearia)
admin.site.register(Administrador)
admin.site.register(Barbeiro)
admin.site.register(Servico)
admin.site.register(Cliente)
admin.site.register(Agendamento)
admin.site.register(Pagamento)