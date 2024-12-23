import os
import time

import requests

from pydantic import EmailStr, NameEmail
from services.sendmail.schemas.sendmail import EnqueueResponse

current_file_path = os.path.abspath(os.path.dirname(__file__))
from .test_base_tenants import TestBaseTenantsAPIV2


class TestSVC(TestBaseTenantsAPIV2):
    services = ['tenants', 'sendmail']

    async def setup(self):
        await super().setup()

    async def test_is_sendmail_healthy(self):
        response = await self.request(method='get', url="/api/sendmail/healthy", headers={'X-Tenant-ID': 'pass'})
        assert response.status_code == 200

    # @enable_emailing_in_test_mode
    async def test_enqueue_email(self):
        from shared.services.sendmail.schemas.email_schema import EmailRequest

        email_request = EmailRequest(
            sender=NameEmail(name='Igor Jeremic', email='info@digitalcube.rs'),
            to=[NameEmail(name='Igor Jeremic', email='igor@digitalcube.rs')],
            subject='CCC Test Subject',
            body='Test Body')

        await self.request(method='post',
                           url="/api/sendmail/enqueue",
                           model_data=email_request,
                           response_format_schema=EnqueueResponse
                           )

        assert self.last_status_code == 200

        await self.request(method='post', url="/api/sendmail/send-next",
                                      model_data=email_request)

        assert self.last_status_code == 200


    # async def test_send_email(self):
