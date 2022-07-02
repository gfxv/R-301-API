from pydantic import BaseModel
from typing import Union

class Carbine(BaseModel):
    barrel: Union[str, None] = None
    mag: Union[str, None] = None
    stock: Union[str, None] = None
    optics: Union[str, None] = None