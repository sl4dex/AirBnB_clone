from models.base_model import BaseModel
class State(BaseModel):
    """class State"""
    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__()
