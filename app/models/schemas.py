from pydantic import BaseModel, HttpUrl

class Project(BaseModel):
    title: str
    description: str
    stack: list[str]
    repo: HttpUrl | None = None
    demo: HttpUrl | None = None
