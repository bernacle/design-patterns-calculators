from typing import Dict, List
from pytest import raises
from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError():
    def variance(self, numbers: List[float]) -> float:
        return 3
    
class MockDriverHandler():
    def variance(self, numbers: List[float]) -> float:
        return 100000


def test_calculate_with_variance_rror():
    mock_request = MockRequest(body={ "numbers": [1.23, 2.34, 3.45] })
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as exception:
        calculator_3.calculate(mock_request)

    assert str(exception.value) == "variance is less than multiply result"

def test_calculate():
    mock_request = MockRequest(body={ "numbers": [1, 1, 1, 1, 100] })
    calculator_3 = Calculator3(MockDriverHandler())
    response =  calculator_3.calculate(mock_request)
    assert response == {'data': {"calculator": 3, 'value': 100000, 'success': True}}
