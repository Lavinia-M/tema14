from clase_pt_test import Angajat
import pytest
from unittest.mock import patch


@pytest.fixture
def angajat():
    angajat = Angajat("Popescu", "Ion", 3500)
    return angajat

@patch('builtins.print')
def test_descrie_angajat(mock_print, angajat):
    angajat.descrie()
    mock_print.assert_called_with(f'Angajatul cu numele {angajat.nume} si prenumele {angajat.prenume} '
                                  f'are salariul {angajat.salariu}')

def test_nume_complet_angajat(angajat):
    assert angajat.nume_complet() == "Popescu Ion"

def test_salariu_lunar(angajat):
    assert angajat.salariu_lunar() == 3500

def test_salariu_anual(angajat):
    assert angajat.salariu_anual() == 42000