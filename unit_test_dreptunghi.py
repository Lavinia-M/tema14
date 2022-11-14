import pytest
from clase_pt_test import Dreptunghi
from unittest.mock import patch


@pytest.fixture
def dreptunghi():
    dreptunghi = Dreptunghi(5, 10, "rosu")
    return dreptunghi


@patch('builtins.print')
def test_descrie_dreptunghi(mock_print, dreptunghi):
    dreptunghi.descrie()
    mock_print.assert_called_with(f'Dreptunghiul are culoarea {dreptunghi.culoare}, are lungimea {dreptunghi.lungime} '
                                  f'si latimea {dreptunghi.latime}')


def test_aria_dr(dreptunghi):
    assert dreptunghi.aria() == 50


def test_perimetrul_dr(dreptunghi):
    assert dreptunghi.perimetru() == 30


def test_schimba_culoarea_dr(dreptunghi):
    dreptunghi.schimba_culoarea("albastru")
    dreptunghi.descrie()



