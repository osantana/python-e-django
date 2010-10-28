# -*- encoding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class ItemAgenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    usuario = models.ForeignKey(User)
    participantes = models.ManyToManyField(User,
                           related_name='item_participantes')

    def __unicode__(self):
        return u"Titulo: %s Data/Hora:%s / %s" % (
                self.titulo, self.data, self.hora)


# Funções que tratam sinais podem receber parâmetros
# diferentes em situações distintas. Neste caso, o mais seguro
# é receber um parâmetro do tipo **kwargs
def envia_email(**kwargs):
    try:
        # O objeto sendo gravado vem no parâmetro instance
        item = kwargs['instance']
    except KeyError:
        return

    for participante in item.participantes.all():
        if participante.email:
            dados = {
                'titulo': item.titulo,
                'data': datetime.strftime(item.data, "%d/%m/%Y"),
                'hora': item.hora,
                'descricao': item.descricao,
            }
            subject = "[evento] %(titulo)s dia %(data)s as %(hora)s"
            message = ("Evento: %(titulo)s\n"
                       "Dia: %(data)s\n"
                       "Hora: %(hora)s\n"
                       "\n"
                       "%(descricao)s")
            participante.email_user(
                subject=subject % dados,
                message=message % dados,
                from_email=item.usuario.email
            )

models.signals.post_save.connect(envia_email,
        sender=ItemAgenda,
        dispatch_uid="agenda.models.ItemAgenda")

