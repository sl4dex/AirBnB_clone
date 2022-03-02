from models.base_model import BaseModel
class Amenity(BaseModel):
    """class amenity"""

    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__()
