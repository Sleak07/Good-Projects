#TODO: Create a validation for input string system

from pydantic import BaseModel,Field,field_validator,ValidationError, model_validator
from pydantic.types import StringConstraints
from typing import Annotated
from enum import Enum

class OperationType(str,Enum):
    """
    Key Value pairs for operation selection 
    
    :var ADD:
    :vartype ADD:
    :var DELETE:
    :vartype DELETE:
    :var REVERSE:
    :vartype REVERSE:
    :var EXIT:
    :vartype EXIT:
    """
    ADD = "ADD"
    DELETE = "DELETE"
    REVERSE = "REVERSE"
    EXIT = "EXIT"


class DNAInput(BaseModel):
    seq : Annotated[
    str,
    StringConstraints(
        strip_whitespace= True,
        min_length= 3,
        max_length= 100,
        pattern= r"^[ATGCatgc\s]+$"
    ),
]

    @field_validator("seq")
    @classmethod
    def clean_sequence(cls,v:str)-> str:
        return v.replace(" ","").upper()

#Range validation
class DNARange(BaseModel):

    seq: D
    start_pos: int = Field(...,ge=1,le=100,description="Starting Index(1-based)")
    length : int = Field(...,ge=1,le=100,description="Length of  segment")

    @model_validator(mode="after")
    def check_length_sequence(self):
        
        
