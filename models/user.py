from models.base_model import BaseModel
class User(BaseModel):
    """class user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__()