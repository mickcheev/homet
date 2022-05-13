from pydantic import BaseModel, Field


class NewNote(BaseModel):
    title: str = Field(max_length=120)
    content: str = Field()
    node: int = Field()


class EditNote(BaseModel):
    id: int
    new_content: str = Field()
    new_title: str = Field()


class NewNode(BaseModel):
    name: str = Field(max_length=40)
    parent: int
