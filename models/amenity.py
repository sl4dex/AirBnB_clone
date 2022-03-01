from models.base_model import BaseModel
class Amenityr(BaseModel):
    """class user"""

    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__()