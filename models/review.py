from models.base_model import BaseModel
class Review(BaseModel):
    """class Review"""

    place_id = ""
    user_id = ""
    txt = ""
    def __init__(self, *args, **kwargs):
        super().__init__()