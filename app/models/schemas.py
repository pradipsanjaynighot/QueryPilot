from pydantic import BaseModel,Field
class TestResponse(BaseModel):
    message:str
    success:bool

class QueryRequest(BaseModel):
    question:str=Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Natural language question asked by the user."
    )

class SQLResponse(BaseModel):
    sql:str=Field(
        ...,
        min_length=1,
        description="Sql query generated from users natural language request."
    )
    explanation:str=Field(
        ...,
        min_length=1,
        description="uman readable explanation of the generated sql."
    )