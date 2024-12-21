import uuid
from typing import Optional

import pydantic


class EnqueueResponse(pydantic.BaseModel):
    id: uuid.UUID
    message: str

class SendNextResponse(pydantic.BaseModel):
    id: Optional[uuid.UUID|None]=None
    status: str