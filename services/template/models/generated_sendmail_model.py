# THIS IS AN AUTO-GENERATED AND PROTECTED FILE. PLEASE USE
# THE bmanager compile-env SCRIPT TO GENERATE THIS FILE. DO NOT EDIT DIRECTLY
# AS IT CAN BE OVERWRITTEN.
#
# FILE GENERATED ON: 2024-12-22 15:07:12.797695

import tortoise
from base4.models.base import *
from tortoise import fields
from tortoise.fields import CASCADE, RESTRICT
from tortoise.models import Model


class Option(Base, Model):

    class Meta:
        table = "sendmail_options"
        app = "sendmail"

    key = fields.CharField(255, null=False, unique=True)
    value = fields.TextField(null=True)

    mk_cache_rules = []

    @staticmethod
    def schema_service_loc():
        return None

    schema_loc_dict = {'created': 'created', 'last_updated': 'last_updated', 'key': 'key', 'value': 'value'}


class Template(Base, Model):

    class Meta:
        table = "sendmail_templates"
        app = "sendmail"

    code = fields.CharField(255, null=False, unique=True)
    name = fields.CharField(255, null=False)
    subject = fields.CharField(255, null=False, unique=True)
    body = fields.TextField(null=False)
    variables = fields.JSONField(null=False)

    mk_cache_rules = []

    @staticmethod
    def schema_service_loc():
        return None

    schema_loc_dict = {
        'created': 'created',
        'last_updated': 'last_updated',
        'code': 'code',
        'name': 'name',
        'subject': 'subject',
        'body': 'body',
        'variables': 'variables',
    }


class Mailqueue(Base, Model):

    class Meta:
        table = "sendmail_mailqueue"
        app = "sendmail"

    sender = fields.CharField(255, null=False)
    reply_to = fields.CharField(255, null=True)
    to = fields.JSONField(null=False)
    cc = fields.JSONField(null=True)
    bcc = fields.JSONField(null=True)
    subject = fields.CharField(255, null=True)
    body = fields.TextField(null=True)
    template = fields.ForeignKeyField('sendmail.Template', null=True, index=True, on_delete=tortoise.fields.base.OnDelete.RESTRICT, related_name='mailqueue')

    mk_cache_rules = []

    @staticmethod
    def schema_service_loc():
        return None

    schema_loc_dict = {
        'created': 'created',
        'last_updated': 'last_updated',
        'sender': 'sender',
        'reply_to': 'reply_to',
        'to': 'to',
        'cc': 'cc',
        'bcc': 'bcc',
        'subject': 'subject',
        'body': 'body',
        'template_id': 'template_id',
    }
