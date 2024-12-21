from typing import Dict
from urllib.request import Request
from base4.service.exceptions import ServiceException
import os
from base4.service.base import BaseService
from fastapi.exceptions import HTTPException
import dotenv
import services.sendmail.models as models
import services.sendmail.schemas as schemas
from base4.utilities.db.async_redis import get_redis

from shared.services.sendmail.schemas.email_schema import EmailRequest


from ._db_conn import get_conn_name

dotenv.load_dotenv()
default_id_user = os.getenv('DEFAULT_ID_USER', '00000000-0000-0000-0000-000000000000')


class SendmailService(BaseService[models.Mailqueue]):
    def __init__(self):
        super().__init__(schemas.MailQueueSchema, models.Mailqueue, get_conn_name())

    async def send_next(self, request: Request) -> schemas.SendNextResponse:

        from shared.services.sendmail.sendmail import smtp_connect_and_send_message

        async with get_redis() as redis:
            email = await redis.lpop('mailqueue')
            if not email:
                raise ServiceException('NO_EMAIL', 'No Email to be sent', 404)

            res = await smtp_connect_and_send_message(email['mime'])

            ...

        return schemas.SendNextResponse(
            id=email['id'],
            status='tbd')


    async def enqueue(self, request: Request, email_request: EmailRequest) -> schemas.EnqueueResponse:

        email = self.model(
            logged_user_id=default_id_user,
            sender=email_request.sender.email,
            reply_to=email_request.reply_to.email if email_request.reply_to else None,
            to=[e.email for e in email_request.to] if email_request.to else None,
            cc=[e.email for e in email_request.cc] if email_request.cc else None,
            bcc=[e.email for e in email_request.bcc] if email_request.bcc else None,
            subject=email_request.subject,
            body=email_request.body,
            template=email_request.template
        )
        await email.save()

        from shared.services.sendmail.sendmail import enqueue_to_redis
        try:
            email_request.id = str(email.id)
            await enqueue_to_redis(email_request)
        except Exception as e:
            raise

        return schemas.EnqueueResponse(
            message='enqueued',
            id=email.id
        )