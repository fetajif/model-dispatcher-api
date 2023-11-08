class ErrorResponse:
    status: int
    msg: str
    def __init__(self, status = 404, msg = "Error Model Not Found"):
        self.status = status
        self.msg = msg