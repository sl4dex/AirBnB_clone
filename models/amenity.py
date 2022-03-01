from models.base_model import BaseModel
class Amenity(BaseModel):
    """class amenity"""

    name = ""
    def __init__(self, *args, **kwargs):
        super().__init__()
