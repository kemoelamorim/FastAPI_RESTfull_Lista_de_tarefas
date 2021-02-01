from starlette.testclient import TestClient
from starlette.status_code import HTTP_200_OK
from gerenciador_tarefas.gerenciador import app


def test_quando_listar_tarefas_devo_retornar_codigo_de_status_ok():
    cliente = TestClient(app)
    resposta = cliente.get("/tarefas")
    assert resposta.status_code == HTTP_200_OK