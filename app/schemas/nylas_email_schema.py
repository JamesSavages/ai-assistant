from pydantic import BaseModel, Field
from typing import Optional

class EmailObject(BaseModel):
    attachments: list = []
    bcc: list = []
    body: str
    cc: list = []
    date: int
    folders: list = []
    from_: list = Field(..., alias="from")
    grant_id: str
    id: str
    object: str
    reply_to: list = []
    snippet: Optional[str] = None
    starred: bool
    subject: str
    thread_id: str
    to: list
    unread: bool
