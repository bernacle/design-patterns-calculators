class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422


try:
    print("in try")
    raise HttpUnprocessableEntityError("body malformed")
except Exception as exception:
    print("in except")
    print(str(exception))
    print(str(exception.name))
    print(str(exception.status_code))
    print(str(exception.message))
   