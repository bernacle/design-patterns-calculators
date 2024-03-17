from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface  

class Calculator3: 
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiply_result = self.__multiply_rules(input_data)
        self.__verify_result(variance, multiply_result)
        formatted_response = self.__format_response(variance)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body malformed")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance =  self.__driver_handler.variance(numbers)
        return variance
    
    def __multiply_rules(self, numbers: List[float]) -> float:
        multiply_result = 1
        for number in numbers: multiply_result *= number
        return multiply_result
    
    def __verify_result(self, variance: float, multiply_result: float ) -> None:
        if variance < multiply_result:
            raise Exception("variance is less than multiply result")
    
    def __format_response(self, variance: float) -> Dict:
        return {
            "data" : {
                "calculator" : 3,
                "value" : variance,
                "success": True
            }
        }