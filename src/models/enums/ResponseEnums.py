from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATION_ERROR="File Validation Error"
    FILE_DELETED_SUCCESS="File Validation Success"

    FILE_TYPE_NOT_SUPPORTED="File Type Not Supported"
    FILE_SIZE_EXCEEDED="File Size Exceeded"
    FILE_UPLOAD_SUCCESS="File Upload Success"
    FILE_UPLOAD_FAILED="File Upload Failed"
    FILE_DELETED_SUCCESS="File Deleted Success"
    FILE_DELETED_FAILED="File Deleted Failed"
    FILE_NOT_FOUND="File Not Found"
    
    