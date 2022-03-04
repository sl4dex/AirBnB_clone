from models.base_model import BaseModel


class State(BaseModel):
    """class State"""
    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(*args, **kwargs)
