from typing import Dict
from pytest import raises
from src.calculators.calculator_2 import Calculator2

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={ "numbers": [1.23, 2.34, 3.45] })
    calculator_2 = Calculator2()
    response =  calculator_2.calculate(mock_request)

    assert isinstance(response, dict)

    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]
    
    assert response["data"]["result"] == 0.12
    assert response["data"]["calculator"] == 2

def test_calculate_with_body_error():
    mock_request = MockRequest(body={ "number": 1 })

    calculator_2 = Calculator2()

    with raises(Exception) as excinfo:
        calculator_2.calculate(mock_request)

    assert str(excinfo.value) == "body malformed"