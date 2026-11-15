from pydantic import BaseModel, Field, HttpUrl

class ServicoCreate(BaseModel):
    nome: str = Field(min_length=1, max_length=100)
    url : HttpUrl
    intervalo_segundos : int = Field(default=60, ge = 30, le=3600)

class ServicoOut(BaseModel):

    id:int
    nome:str
    url:str
    intevalo_segundos: int
    ativo:bool