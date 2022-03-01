from models.base_model import BaseModel
class User(BaseModel):
    """class user"""

    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__()