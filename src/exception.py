import sys
import logging


def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    error_file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    
    error_massage= "Error occured in python script name [{0}] line number [{1}] error message is [{2}]".format(
        error_file_name, line_no, error
    )
    return error_massage
    
class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail=error_detail)
        
    def __str__(self) -> str:
        return self.error_message
    
