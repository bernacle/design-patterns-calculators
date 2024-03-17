from typing import Dict, List
from pytest import raises
from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3


def test_calculate_integration():
    mock_request = MockRequest(body={ "numbers": [1.23, 2.34, 3.45] })
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    response =  calculator_2.calculate(mock_request)

    assert isinstance(response, dict)

    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]
    
    assert response["data"]["result"] == 0.12
    assert response["data"]["calculator"] == 2

def test_calculate():
    mock_request = MockRequest(body={ "numbers": [1, 2, 3] })
    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    formatted_response = calculator_2.calculate(mock_request)
    assert "data" in formatted_response
    assert "calculator" in formatted_response["data"]
    assert "result" in formatted_response["data"]
    
    assert formatted_response["data"]["result"] == 0.33
    assert formatted_response["data"]["calculator"] == 2
