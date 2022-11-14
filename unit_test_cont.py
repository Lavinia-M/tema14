from clase_pt_test import Cont
import pytest
from unittest.mock import patch

@pytest.fixture
def cont():
    cont = Cont("RO25btrlroncrt12865958", "Popescu Ion", 1000)
    return cont

@patch('builtins.print')
def test_afisare_sold(mock_print, cont):
    cont.afisare_sold()
    mock_print.assert_called_with(f'Titularul {cont.titular_cont} are in contul {cont.iban} '
                                   f'suma de {cont.sold} lei.')

def test_debitare_sold(cont):
    cont.debitare_cont(100)
    assert cont.sold == 900


def test_creditare_sold(cont):
    cont.creditare_cont(500)
    assert cont.sold == 1500