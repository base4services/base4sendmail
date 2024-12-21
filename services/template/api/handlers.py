
from base4.utilities.service.base import api, route
from base4.utilities.service.base import BaseAPIHandler
from fastapi import Request, APIRouter
from services.sendmail.services.sendmail import SendmailService
import base4.service.exceptions

from shared.services.sendmail.schemas.email_schema import EmailRequest

@route(router=APIRouter(), prefix='/api/sendmail')
class SendMailAPIHandler(BaseAPIHandler):

    def __init__(self, router):

        self.service = SendmailService()
        super().__init__(router)

    @api(
        method='POST',
        path='/enqueue',
    )
    async def enqueue(self, request: Request, data: EmailRequest): # -> EnqueueResponse

        try:
            return await self.service.enqueue(request, data)
        except base4.service.exceptions.ServiceException as se:
            raise se.make_http_exception()
        except Exception as e:
            raise base4.service.exceptions.HTTPException(500,
                                                         detail={'code': 'INTERNAL_SERVER_ERROR', 'message': str(e)})


    @api(
        method='POST',
        path='/send-next',
    )
    async def send_next(self, request: Request): # -> EnqueueResponse

        try:
            return await self.service.send_next(request)
        except base4.service.exceptions.ServiceException as se:
            raise se.make_http_exception()
        except Exception as e:
            raise base4.service.exceptions.HTTPException(500,
                                                         detail={'code': 'INTERNAL_SERVER_ERROR', 'message': str(e)})

