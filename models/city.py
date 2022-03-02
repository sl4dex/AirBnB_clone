from models.base_model import BaseModel
class City(BaseModel):
    """class City"""

    def __init__(self, *args, **kwargs):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        super().__init__()