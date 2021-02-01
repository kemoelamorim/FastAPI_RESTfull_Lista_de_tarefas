from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK

def test_quando_listar_tarefas_devo_retornar_codigo_de_status_ok():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.status == HTTP_200_OK