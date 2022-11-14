from clase_pt_test import Cerc
import pytest
from unittest.mock import patch


@pytest.fixture
def cerc():
    cerc = Cerc(4, "verde")
    return cerc

@patch('builtins.print')
def test_descrie_cerc(mock_print, cerc):
    cerc.descrie_cerc()
    mock_print.assert_called_with(f'Culoarea cercului este {cerc.culoare} si raza cercului este {cerc.raza}')


def test_diametru_cerc(cerc):
    assert cerc.diametru() == 8
