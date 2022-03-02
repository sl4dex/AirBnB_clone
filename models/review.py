from models.base_model import BaseModel
class Review(BaseModel):
    """class Review"""


    txt = ""
    def __init__(self, *args, **kwargs):
        place_id = ""
        user_id = ""
        super().__init__()