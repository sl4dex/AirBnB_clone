from models.base_model import BaseModel
class Review(BaseModel):
    """class Review"""


    txt = ""
    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        super().__init__()