import pytest

# ja que a chanada para o teste eh chamado na raiz do projeto
# este import pode ser feito sem necessitar do uso de sys.path
from pacote.classe import Pessoa

# autouse=True informa que esta fixture deve ser utilizada sem ter de informar explicitamente no metodo de teste
# scope='module' informa que a fixture deve ser utilizada em modulos
# o codigo apos o 'yield' sera executado ao fim do teste (no escopo informado)
@pytest.fixture(autouse=True, scope='module')
def setup():
  print('inicio')
  yield
  print('fim')

# Define esta funcao como sendo da marca 'caso1'.
# Com isso, todas as funcoes marcadas com 'caso1'
# podem ser executadas com: pytest -m caso1
@pytest.mark.caso1
def test_soma(entrada):
  assert entrada + entrada == entrada*2

# Marca a funcao como 'caso2'
# Pode ser executada com: pytest -m caso2
@pytest.mark.caso2
def test_subtracao(entrada):
  p = Pessoa()
  print(p.nome)
  assert entrada - entrada == entrada-entrada
