from models.base_model import BaseModel
class Amenity(BaseModel):
    """class amenity"""

    def __init__(self, *args, **kwargs):
        name = ""
        super().__init__()
