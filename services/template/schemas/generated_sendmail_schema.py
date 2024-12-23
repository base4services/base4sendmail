# THIS IS AN AUTO-GENERATED AND PROTECTED FILE. PLEASE USE
# THE compile-yaml SCRIPT TO GENERATE THIS FILE. DO NOT EDIT DIRECTLY
# AS IT CAN BE OVERWRITTEN.
#
# FILE GENERATED ON: 2024-12-22 15:07:13.062596


import datetime
import uuid
from typing import Any, AnyStr, Dict, List, Literal, Optional

from base4.project_specifics import lookups_module as Lookups
from base4.schemas.base import NOT_SET, Base
from fastapi.requests import Request
from pydantic import BaseModel, field_validator


class OptionSchema(Base):
    key: str
    value: str

    @classmethod
    def check_existence_rules(cls):
        return {}

    @classmethod
    def model_loc(cls):
        return {
            'created': 'created',
            'last_updated': 'last_updated',
            'is_deleted': 'is_deleted',
            'deleted': 'deleted',
            'id': 'id',
            'key': 'key',
            'value': 'value',
        }

    @classmethod
    def schema_class_loc(cls):
        return {
            "key": str,
            "value": str,
        }


class TemplateSchema(Base):
    code: str
    name: str
    subject: str
    body: str
    variables: dict

    @classmethod
    def check_existence_rules(cls):
        return {}

    @classmethod
    def model_loc(cls):
        return {
            'created': 'created',
            'last_updated': 'last_updated',
            'is_deleted': 'is_deleted',
            'deleted': 'deleted',
            'id': 'id',
            'code': 'code',
            'name': 'name',
            'subject': 'subject',
            'body': 'body',
            'variables': 'variables',
        }

    @classmethod
    def schema_class_loc(cls):
        return {
            "code": str,
            "name": str,
            "subject": str,
            "body": str,
            "variables": dict,
        }


class MailQueueSchema(Base):
    sender: str
    reply_to: str
    to: list
    cc: Optional[list | None | Literal[NOT_SET]] = NOT_SET
    bcc: Optional[list | None | Literal[NOT_SET]] = NOT_SET
    subject: str
    template: Optional[TemplateSchema | None | Literal[NOT_SET]] = NOT_SET

    @classmethod
    def check_existence_rules(cls):
        return {}

    @classmethod
    def model_loc(cls):
        return {
            'created': 'created',
            'last_updated': 'last_updated',
            'is_deleted': 'is_deleted',
            'deleted': 'deleted',
            'id': 'id',
            'sender': 'sender',
            'reply_to': 'reply_to',
            'to': 'to',
            'cc': 'cc',
            'bcc': 'bcc',
            'subject': 'subject',
            'template': 'template',
        }

    @classmethod
    def schema_class_loc(cls):
        return {
            "sender": str,
            "reply_to": str,
            "to": list,
            "cc": list,
            "bcc": list,
            "subject": str,
            "template": TemplateSchema,
        }
