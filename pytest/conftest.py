import pytest

# fixture que eh utilizada por diferentes modulos sao definidas aqui
# fixtures sao chamadas informando no parametro da funcao de teste
@pytest.fixture
def entrada():
  return 2

# fixture utilizada sem ter de ser passada por parametro na funcao de teste
@pytest.fixture(autouse=True)
def setup():
  print('inicio')
  yield
  print('fim')
