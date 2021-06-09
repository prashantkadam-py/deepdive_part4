from datetime import datetime

class APIException(Exception):
    "Base API Exception"
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "API exception occured"
    user_err_msg = "We are sorry! An unexcepted error occurred on our end."

    def __init__(self, *args, user_err_msg=None):
        if args:
            self.internal_err_msg= args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg:
            self.user_err_msg = user_err_msg

    def to_json(self):
        err_object = {
                        "status" : self.http_status,
                        "message" : self.user_err_msg
                        }
        return json.dumps(err_object)


    def log_exception(self):
        exception = {
                "type" : type(self).__name__,
                "http_status" : self.http_status,
                "message" : self.args[0] if self.args else self.internal_err_msg,
                "args" : self.args[1:]
                }

        print(f"EXCEPTION : {datetime.utcnow().isoformat()} {exception}")
            


class ApplicationException(APIException):
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = "Generic server side exception"
    user_err_msg = "We are sorry!! An unexpected error occurred at our end."

