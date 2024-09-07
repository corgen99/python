import factorielle
import sys
from io import StringIO

def test_erreur_nombre_negatif(mocker):
    mocker.patch('builtins.input', return_value="-1")
    captured_output=StringIO()
    sys.stdout=captured_output
    factorielle.main()
    output=captured_output.getvalue()
    sys.stdout=sys.__stdout__
    expected_value="Erreur ! Le nombre doit être un entier positif."
    assert expected_value in output

def test_erreur_booleen(mocker):
    mocker.patch('builtins.input', return_value="True")
    captured_output=StringIO()
    sys.stdout=captured_output
    factorielle.main()
    output=captured_output.getvalue()
    sys.stdout=sys.__stdout__
    expected_value="Erreur ! La valeur fournie n'est pas un nombre entier, essayez encore..."
    assert expected_value in output

def test_erreur_float(mocker):
    mocker.patch('builtins.input', return_value="1.5")
    captured_output=StringIO()
    sys.stdout=captured_output
    factorielle.main()
    output=captured_output.getvalue()
    sys.stdout=sys.__stdout__
    expected_value="Erreur ! La valeur fournie n'est pas un nombre entier, essayez encore..."
    assert expected_value in output

def test_erreur_char(mocker):
    mocker.patch('builtins.input', return_value="e")
    captured_output=StringIO()
    sys.stdout=captured_output
    factorielle.main()
    output=captured_output.getvalue()
    sys.stdout=sys.__stdout__
    expected_value="Erreur ! La valeur fournie n'est pas un nombre entier, essayez encore..."
    assert expected_value in output

def test_factorielle(mocker):
    mocker.patch('builtins.input', return_value="5")
    captured_output=StringIO()
    sys.stdout=captured_output
    factorielle.main()
    output=captured_output.getvalue()
    sys.stdout=sys.__stdout__
    expected_value="120"
    assert expected_value in output