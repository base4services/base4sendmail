from base4.utilities.service.base import api, route, BaseAPIHandler
from fastapi import Request, APIRouter
from services.sendmail.services.sendmail import SendmailService
import base4.service.exceptions

router = APIRouter()

from shared.services.sendmail.schemas.email_schema import EmailRequest

@route(router=router, prefix='/api/sendmail')
class SendMailAPIHandler(BaseAPIHandler):

    def __init__(self, router):
        super().__init__(router, service=SendmailService(), schema=EmailRequest, model=None)


    @api(
        is_public=False,
        method='POST',
        path='/enqueue',
    )
    async def enqueue(self, request: Request, data: EmailRequest): # -> EnqueueResponse

        try:
            return await self.service.enqueue(request, email_request=data)

        except base4.service.exceptions.ServiceException as se:
            raise se.make_http_exception()

        except Exception as e:
            raise base4.service.exceptions.HTTPException(500,  detail={'code': 'INTERNAL_SERVER_ERROR', 'message': str(e)})


    @api(
        is_public=False,
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

