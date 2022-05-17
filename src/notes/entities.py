from pydantic import BaseModel, Field


class NewNote(BaseModel):
    title: str = Field(max_length=120)
    content: str


class EditNote(BaseModel):
    id: int
    new_content: str = Field()
    new_title: str = Field()


class NewNode(BaseModel):
    name: str = Field(max_length=40)
    parent: int


class GetNote(BaseModel):
    content: str = Field(default=None)
    created: str = Field(default=None)
    last_changed: str = Field(default=None)
    title: str = Field(default=None)
    id: int = Field(default=None)
