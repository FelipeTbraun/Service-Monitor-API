from fastapi import APIRouter

from app.schemas import ServicoCreate, ServicoOut

#APIRouter = Grupo de rotas, no prefix de servicos, todas as rotas comecarão com /servicos/...
router = APIRouter(prefix="/servicos", tags=["servicos"])

#Por enquanto guarda em memoria (mudar depois) prefixo de _ significa que é uma funcao provisoreio que so irá ser usado aqui ou em um lugar especifico
_servicos: list[dict] = []

#Rota vazia: ""; ServicoOut formata a resposta no modelo de /docs e status 201 = sucesso
@router.post("", response_model=ServicoOut, status_code=201)
def criar_servico(dados : ServicoCreate):
    novo = {
        #len servicos + 1 é a qtd atual de itens + 1, str() converte para string, que é o esperado pelo ServicoOut
        "id": len(_servicos) + 1,
        "nome": dados.nome,
        "url": str(dados.url),
        "intervalo_segundos": dados.intervalo_segundos,
        "ativo": True,

    }
    _servicos.append(novo)
    return novo

@router.get("", response_model=list[ServicoOut])
def listar_servicos():
    return _servicos