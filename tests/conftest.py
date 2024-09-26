import pytest

@pytest.fixture(scope='session')
def setup_environment():
    print("\n Configurando el entorno de pruebas...")

