from models.base_model import BaseModel
class User(BaseModel):
    """class user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        super().__init__()