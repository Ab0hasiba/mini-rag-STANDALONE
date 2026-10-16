from fastapi import UploadFile
from controllers.BaseController import BaseController
class DataController(BaseController):

    def __init__(self):
        super().__init__()
        self.size_scale=1048576
        
    def validate_upload_file(self,file:UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        if file.size > self.app_settings.FILE_MAX_SiZE*self.size_scale:
            return False
        return True