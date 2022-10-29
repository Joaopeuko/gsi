from pydantic import BaseModel, Field


class InputPredict(BaseModel):
    owner: str = Field(description="This parameter receives the name of the repository owner")
    repo: str = Field(description="This parameter receives the name of the repository")
    pages_amount: int = Field(description="This parameter is how many pages do you want to extract information")